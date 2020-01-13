from random import randint

def checkWin(board, player):
    for i in range(0, 7, 3):
        if(board[i] == player and board[i+1] == player and board[i+2] == player):
            return True
    for i in range(0, 3):
        if(board[i] == player and board[i+3] == player and board[i+6] == player):
            return True
    if(board[0] == player and board[4] == player and board[8] == player):
        return True
    if(board[2] == player and board[4] == player and board[6] == player):
        return True
    return False

def checkLose(board, player):
    if(player == "X"):
        opponent = "O"
    else:
        opponent = "X"
    if(checkWin(board, opponent)):
        return True
    return False

def checkTie(board):
    for x in board:
        if(x == " "):
            return False
    return True
    

def getAIMove(board, nextMove, aiPlayer):
    if(checkWin(board, aiPlayer)):
        return (-1, 10)
    elif(checkLose(board, aiPlayer)):
        return (-1, -10)
    elif(checkTie(board)):
        return (-1, 0)

    moves = []
    
    for i in range(len(board)):
        if(board[i] == " "):
            board[i] = nextMove
            
            score = getAIMove(board, ("X" if nextMove == "O" else "O"), aiPlayer)[1]
            moves.append((i, score))
            board[i] = " "

    
    if(nextMove == aiPlayer):
        maxScore = moves[0][1]
        bestMove = moves[0]
        for move in moves:
            if(move[1] > maxScore):
                bestMove = move
                maxScore = move[1]
        return bestMove
    else:
        minScore = moves[0][1]
        worstMove = moves[0]
        for move in moves:
            if(move[1] < minScore):
                worstMove = move
                minScore = move[1]
        return worstMove
        


def printBoard(board):
    print("\n")
    for i in range(9):
        if(not board[i] == " "):
            print(board[i], end="   ")
        else:
            print("_", end="   ")
        if(i==2 or i==5):
            print("")
    print("\n")


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while(not (checkWin(board, "O") or checkLose(board, "O") or checkTie(board))):
    playerPosition = int(input("Where do you want to play X: ")) - 1
    board[playerPosition] = "X"
    aiMovePosition = int(getAIMove(board, "O", "O")[0])
    board[aiMovePosition] = "O"
    printBoard(board)
    
