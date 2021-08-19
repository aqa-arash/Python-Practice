import random, colorama
colorama.init(autoreset=True)
black=colorama.Fore.BLACK+colorama.Back.WHITE
red=colorama.Fore.RED+colorama.Back.WHITE
def deck_creator():
    """Creats a full deck set"""

    global deckdic
    deckdic = {}
    #Cards come in 4 suits Spades, Hearts, Clubs and Dianonds
    types= ["S.","H.","C.","D."]
    for type in types:
        for i in range(2,11):
            deckdic[type+str(i)]= i
        deckdic[type+"Ace"]= 11
        deckdic[type+"Jack"]=10
        deckdic[type+"Queen"]=10
        deckdic[type+"King"]=10

def deck_shuffler():
    """recreates and Shuffles the deck"""
    global deck, deckdic,black,red,deckc
    deck=[]
    deckcolor=[]
    for key in deckdic.keys():
        if key[0] in ["S","C"]:
            deckcolor.append(black+key)
        else:
            deckcolor.append(red+key)
        deck.append(key)
    deckc={deck[i]:deckcolor[i] for i in range(len(deck))}
    random.shuffle(deck)

class Bank:
    """Made to hold the bit and player money"""
    def __init__(self,name,balance):
        """Initialize the bank with name of the account and its balance"""
        self.name= name
        self.balance=balance
    def deposit(self,amount):
        """Add money to account"""
        self.balance+=amount
    def withdraw(self,amount):
        """take money from acount"""
        if amount > self.balance:
            print("Insufficient Funds")
            return False
        else:
            self.balance-=amount
    def __str__(self):
        """Print the moeny"""
        return(f" {self.name} : {self.balance} ")
def bet():
    """Takes the player bet"""
    global player,bet
    while True:
        try:
            amount=float(input("How much would you like to bet? "))
        except:
            print("please input a valid number!")
        else:
            if player.balance< amount:
                print("Insufficient Funds! ")
            else:
                player.withdraw(amount)
                pot.deposit(amount)
                break;
def oneortwo(string):
    """Runs an options menu, handles errors"""
    while True:
        try:
            choice=int(input(string))
        except:
            print("please enter the number only")
        else:
            if choice in [1,2]:
                return choice==1
            else:
                print("Enter 1 or 2 only")
                continue
def handcalc(hand):
    """Calculates the value of the hand"""
    global deckdic
    sum=0
    for i in hand:
        sum += deckdic[i]
    while sum >21:
        for i in ["D.Ace","H.Ace","S.Ace","C.Ace"]:
            if i in hand:
                sum-=10
        else:
            break
    return sum

def AI(playerhand):
    """Runs the AI for the game"""
    global deckdic,deck,tablehand,player
    target= handcalc(playerhand)
    while handcalc(tablehand)<target:
        tablehand.append(deck.pop())
    th=[]
    for i in tablehand:
        th.append(deckc[i])
    print("House Hand \n"+ " - ".join(th))
    if handcalc(tablehand)>21:
        print("House goes Bust! You Win! ")
        player.deposit(pot.balance*2)
    elif handcalc(playerhand)==handcalc(tablehand):
        print("It's a draw!")
        player.deposit(pot.balance)
    elif handcalc(playerhand)<handcalc(tablehand):
        print("You lose!")

def game():
    global player,pot,deck,tablehand,deckc
    deck_shuffler()
    playerhand=[]
    tablehand=[]
    pot=Bank("Pot",0)
    print(player,pot)
    bet()
    print(player,pot)
    playerhand.append(deck.pop())
    hitornot=True
    while hitornot:
        playerhand.append(deck.pop())
        ph=[]
        for i in playerhand:
            ph.append(deckc[i])
        print("Your hand \n" + " - ".join(ph))
        if handcalc(playerhand) > 21:
            print("Bust")
            break;
        hitornot=oneortwo("Enter 1 to hit or 2 to stand ")
    else:
        AI(playerhand)
    print(player)


#Main code!
print("This is a terminal-based Black Jack game!")
print("House cheats! It knows where you stand and will try to beat you.")
print("You start with 1000$, you can easily cheat by editing the code!")
player=Bank(input("Please enter your name : "),1000)
playagain=True
deck_creator()
while playagain:
    game()
    if player.balance==0:
        print("Your are out of money!")
        break
    playagain=oneortwo("Continue? Enter 1 for yes or 2 for no! ")
print(f"you came out with {player.balance}$")
if player.balance>1000:
    print(f"You made {player.balance-1000}, Congratulations {player.name}!")
else:
    print(f"I hope you enjoyed the game, {player.name}!")
input(" ")
