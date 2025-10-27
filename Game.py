board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

player_one = "X"
player_two = "0"
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
def player1Input(board):
    place= int(input("enter a number 1-9: "))
    if place <= 1 and place <= 9 and board[place-1] == "-":
        board[place-1]=player_one
    else:
        print("Spot alraedy take try again")

# ask player two to play
def player2Input(board):
    place= int(input("enter a number 1-9: "))
    if place <= 1 and place <= 9 and board[place-1] == "-":
        board[place-1]=player_two
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
        Winner = board[8]
        return True
    
