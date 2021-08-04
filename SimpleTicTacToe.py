#choose your markers
def marks():
    """
    Let's players choose their Icons
    """
    global x,o
    x = input('Player 1 choose your mark :  ')
    o = input('Player 2 choose your mark :  ')
    while x==o :
        o = input('Player 2 choose your mark, that one is taken')
# Ready to play?
def start():
    """
    Starts the game engine and allows replays
    """
    global x,o
    mar=input ("Would you like to choose your icons? (y/n)  ")
    if mar.lower() == "y":
        marks()
    else:
        if mar.lower()!="n":
            print("I take that as a no! ")
        x="X"
        o="O"
    ready=input("Are you ready to play? (y/n) ")
    if ready.lower() == "y":
        return True
    else:
        if ready.lower()!="n":
            print("I take that as a no! ")
        return False


#verify place selection
def verify (place,turn):
    """
    Verifies that players have chosen an appropriate cell and presents it in the board
    """
    global no,x,o
    try:
        place= int(place)
    except :
        print("Enter a number!")
        return True
    if place not in range(1,10):
        print ("Wrong number")
        return True
    if no[place-1]==x or no[place-1]== o:
        print("Already full")
        return True
    elif turn==1:
        no[place-1]=x
        return False
    else :
        no[place-1]=o
        return False
#game over function
def check_game(turn):
    """
    Checks if the game is over and shows the results
    """
    global no, x,o
    win_condition =[no[0]==no[1]==no[2],no[0]==no[3]==no[6],no[0]==no[4]==no[8],no[1]==no[4]==no[7],no[2]==no[4]==no[6],no[2]==no[5]==no[8],no[3]==no[4]==no[5],no[6]==no[7]==no[8]]
    nums=set(no)
    nums.discard(x)
    nums.discard(o)
    if any(win_condition):
        if turn ==1 :
            print ("Player 2 Wins")
        else:
            print("Player 1 Wins")
        return False
    elif len(nums)==0:
        print ("It's a draw")
        return False
    else:
        return True
#main game
def game(x,o):
    """
    Takes in player Icons and runs the game
    """
    print("Player one goes first")
    global no
    no=[1,2,3,4,5,6,7,8,9]
    turn=1
    dash = "\n" + ("-----" + ("-" * max(len(x),len(o))))*3 + "\n"
    game_not_over = True
    while game_not_over:
        print("\n"*2)
        print(f"  {no[0]}  |  {no[1]}  |  {no[2]}  {dash}  {no[3]}  |  {no[4]}  |  {no[5]}  {dash}  {no[6]}  |  {no[7]}  |  {no[8]}  ")
        ver=True
        game_not_over = check_game(turn)
        if game_not_over == False:
            break
        if turn == 1 :
            while ver:
                place=input("Player 1 choose a tile 1-9 :  ")
                ver=verify(place,turn)
            turn=2
        else:
            while ver:
                place=input("Player 2 choose a tile 1-9 :  ")
                ver=verify(place,turn)
            turn=1

print("This is a Terminal based Tik Tak Toe game ")
ready= start()
while ready:
    print("\n"*20)
    game(x,o)
    ready=start()
