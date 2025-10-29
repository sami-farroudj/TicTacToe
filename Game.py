import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

player = "X"
Winner = None
GameRunning = True
mode = None



#creat Game board
def printBoard(board):
    print( board[0] +" | "+board[1]+" | "+board[2])
    print("----------")
    print( board[3] +" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6] +" | "+board[7]+" | "+board[8])



# ask player one to play 
def playerInput(board):
    place= int(input("enter a number 1-9: "))
    if place >= 1 and place <= 9:
        if board[place-1] == "-":
            board[place-1]=player
        else:
            print("Spot alraedy taken try again")
            playerInput(board)
    
def IAF(board):
   while True :
    place = random.randint(1,9)
    if board[place-1] == "-":
        board[place-1] = "O"
        break





#check if horizntable line are winnig
def horinzontlecheck(board):
    global Winner
    if board[0] == board[1] == board[2] and board[2] != "-":
        Winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[4]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True
    

    # check if rowline is winning 
def rowcheck(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner= board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner= board[1]
        return True
    
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner= board[2]
        return True
    

# check if diag line is winning
def diagcheck(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return True
    


def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"




# check if tie
def checktie(board):
    global GameRunning
    if "-" not in board:
        printBoard(board)
        print("it's a tie ")
        GameRunning = False

def checkwin():
    global GameRunning
    if horinzontlecheck(board) or diagcheck(board) or rowcheck(board):
        printBoard(board)
        print(f'the winner is {Winner}')
        GameRunning = False

def selectmode():
    global mode
    print("1 Player VS Player")
    print("2 Player VS IA easy")
    choice =  input("choise 1 or 2: ")
    if choice == "1":
        mode = "1v1"
    elif choice == "2":
          mode = "1vIAF"
    else:
        selectmode()


selectmode()
while GameRunning:
    printBoard(board)
    
    if mode == "1v1":
        playerInput(board)
    elif mode =="1vIAF":
        if player == "X":
            playerInput(board)
        else:
            IAF(board)
    checkwin()
    checktie(board)
    switchPlayer()

# import random
# def bot(board)
#   random(1-9)