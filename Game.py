board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

player = "X"
Winner = None
GameRunning = True

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
    if place >= 1 and place <= 9 and board[place-1] == "-":
        board[place-1]=player
    else:
        print("Spot alraedy take try again")


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
    
# check if tie
def checktie(board):
    global GameRunning
    if "-" not in board:
        print("it's a tie ")
        GameRunning = False



def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def checkwin():
    global GameRunning
    if horinzontlecheck(board) or diagcheck(board) or rowcheck(board):
        printBoard(board)
        print(f'the winner is {Winner}')
        GameRunning = False


while GameRunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchPlayer()
    