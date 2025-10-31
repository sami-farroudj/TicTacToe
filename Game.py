import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

player = "X"
Winner = None
GameRunning = True
mode = None
signe="O"


#creat Game board
def printBoard(board):
    print( board[0] +" | "+board[1]+" | "+board[2])
    print("----------")
    print( board[3] +" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6] +" | "+board[7]+" | "+board[8])



# ask player one to play 
def playerInput(board):
    while True:
        try:
            place= int(input("enter a number 1-9: "))
            if 1 <= place <= 9:
                if board[place-1] == "-":
                    board[place-1]=player
                    break
                else:
                    print("Spot alraedy taken try again!")
                    playerInput(board)
            else:
                print(f"impossible to play {place} ")
                playerInput(board)
        except ValueError:
            print("Enter a number between 1 and 9!")
# AI EASY
def IAF(board,signe):
   while True :
    place = random.randint(1,9)
    if board[place-1] == "-":
        board[place-1] = signe
        break

# AI MEDIUM
def IAM(board,signe):
    bestScore=-999
    bestmove= None

    for i in range(9):
        if board[i]=="-":
            board[i]=signe
            score=minimax(board, False,True)
            board[i]="-"
            if score> bestScore:
                bestScore=score
                bestmove=i
    if bestmove !=None:
        board[bestmove]=signe

# AI IMPOSSIBLE

def IAI(board,signe):
    bestscore=-999
    bestmove= None

    for i in range(9):
        if board[i]=="-":
            board[i]= signe
            score = minimax(board,False,False)
            board[i]="-"
            if score> bestscore:
                bestscore=score
                bestmove=i
    if bestmove != None:
        board[bestmove]=signe


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
    


# Implanting Minimax ai 
def minimax(board,maxi,medium=False):
    global Winner

    if horinzontlecheck(board) or rowcheck(board) or diagcheck(board):
        if Winner == "O":
            Winner= None
            return 1
        elif Winner == "X":
            Winner= None
            return -1
    
    if  "-" not in board:
        return 0
    

    if maxi== True:
        bestScore= -999
        for i in range(9):
            if board[i]=="-":
                board[i]="O"
                score = minimax(board,False,medium)
                board[i]="-"
                if medium==True:
                    if score <=0 and score > bestScore:
                      bestScore= score
                else:
                    if score > bestScore:
                        bestScore=score
        return bestScore
    
    else:
        bestScore= 999
        for i in range(9):
            if board[i]== "-":
                board[i]="X"
                score=minimax(board,True,medium)
                board[i]="-"
                if score< bestScore:
                    bestScore=score
        return bestScore
    




def switchPlayer():
    global player
    if player == "X":
        player = signe
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
    print("3 Player VS IA medium")
    print("4 Player VS IA impossible")
    choice =  input("choose 1, 2, 3 or 4: ")
    if choice == "1":
        mode = "1v1"
    elif choice == "2":
          mode = "1vIAF"
    elif choice == "3":
        mode = "1vIAM"
    elif choice == "4":
        mode = "1vIAI"
    else:
        selectmode()



# code execution
selectmode()
while GameRunning:
    printBoard(board)
    
    if mode == "1v1":
        playerInput(board)

    elif mode =="1vIAF":
        if player == "X":
            playerInput(board)
        else:
            IAF(board,signe)

    elif mode == "1vIAM":
        if player == "X":
            playerInput(board)
        else:
            IAM(board,signe)

    elif mode == "1vIAI":
        if player == "X":
            playerInput(board)
        else:
            IAI(board,signe)
    checkwin()
    checktie(board)
    switchPlayer()

