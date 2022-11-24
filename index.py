class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def gameStatus(board):
    winningFormations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for formation in winningFormations:
        if(board[formation[0]] == 1 and board[formation[1]] == 1 and board[formation[2]] ==1):
            return 1
    
    for formation in winningFormations:
        if(board[formation[0]] == -1 and board[formation[1]] == -1 and board[formation[2]] == -1):
            return -1
        
    return 0

def printBoard(board, reverse=False):
    print('\n')
    for i in range(3):
        print('| ',end='')
        for j in range(3):
            if(reverse):
                if(board[3*i+j] == 1):
                    print('X', end=' | ')
                elif(board[3*i+j] == -1):
                    print('O', end=' | ')
                else:
                    print(' ', end=' | ')          
            else:
                if(board[3*i+j] == 1):
                    print('O', end=' | ')
                elif(board[3*i+j] == -1):
                    print('X', end=' | ')
                else:
                    print(' ', end=' | ')          

        print('')  
    print('\n')

def computerMakeMove(board):
    max = -1
    position = 0
    positionChanged = False
    for i in range(9):
        if(board[i] == 0):
            boardCopy = board.copy()
            boardCopy[i] = 1
            if(gameStatus(boardCopy)==1):
                position = i
                positionChanged = True
                break
            score = minimax(boardCopy, -1)
            # print(f'Score: {score} for ')
            # printBoard(boardCopy)
            if(score > max):
                positionChanged = True
                position = i

    if(not positionChanged):
        for i in range(9):
            if(board[i] == 0):
                position = i
                break

    return makeMove(board, 1, position)
    
def makeMove(board, player, position):
    """
    Checks if given position is occupied, if not it will set that position as -1 or 1, if it is occupied, it will return False
    """
    if(board[position] == 0):
        boardCopy = board.copy()
        boardCopy[position] = player
        return boardCopy
    else:
        return False

# def minimax(board: list, currentPlayer: int):
    # """
    # \nReturns score of given board
    # \ncurrentPlayer: 1 = Computer, -1 = User
    # """
    # if(0 not in board or gameStatus(board) != 0):
    #     # print(gameStatus(board))
    #     # printBoard(board)
    #     return gameStatus(board)

    # if(currentPlayer == -1):
    #     score = 1
    # else:
    #     score = -1
    
    # for i in range(9):
    #     if(board[i] == 0):
    #         if(currentPlayer == -1):
    #             minimax_score = minimax(makeMove(board, -1, i), currentPlayer*-1)
    #             if(minimax_score < score):
    #                 score = minimax_score
    #         else:
    #             minimax_score = minimax(makeMove(board, 1, i), currentPlayer*-1)
    #             if(minimax_score > score):
    #                 score = minimax_score
    #     else:
    #         continue

    # return score

def minimax(board: list, currentPlayer: int):
    """
    \nReturns score of given board
    \ncurrentPlayer: 1 = Computer, -1 = User
    """
    if(0 not in board or gameStatus(board) != 0):
        # print(gameStatus(board))
        # printBoard(board)
        return gameStatus(board)

    scores = []
    
    for i in range(9):
        if(board[i] == 0):
            if(currentPlayer == -1):
                minimax_score = minimax(makeMove(board, -1, i), currentPlayer*-1)
                scores.append(minimax_score)
            else:
                minimax_score = minimax(makeMove(board, 1, i), currentPlayer*-1)
                scores.append(minimax_score)
        else:
            continue
    # print('currentPlayer ', str(currentPlayer))
    # print(scores)
    # printBoard(board)
    if(currentPlayer == -1):
        return min(scores)
    else:
        return max(scores)


if __name__ == "__main__":
    board = [0,0,0,0,0,0,0,0,0]
    printBoard(board)

    reverse = bool(int(input('Would you like to be Xs or Os (0/1)? ')))

    if(not reverse):
        print("You are X and the computer is O")
    else:
        print("You are O and the computer is X")

    while(0 in board and gameStatus(board) == 0):
        if(not reverse):
            userPos = int(input(bcolors.OKGREEN+"Enter position to place your X (1-9): "+bcolors.ENDC))
            if(board[userPos-1] != 0):
                print(bcolors.WARNING+"Position occupied. Please choose a different position"+bcolors.ENDC)
                continue

            board = makeMove(board, -1, userPos-1) 
            printBoard(board, reverse)
            if(0 not in board or gameStatus(board)!=0):
                break
            print(bcolors.OKBLUE+'Computer thinking...'+bcolors.ENDC)
            board = computerMakeMove(board)       
            printBoard(board, reverse)

        else:
            print(bcolors.OKBLUE+'Computer thinking...'+bcolors.ENDC)
            board = computerMakeMove(board)       
            printBoard(board, reverse)

            if(0 not in board or gameStatus(board)!=0):
                break

            userPos = int(input(bcolors.OKGREEN+"Enter position to place your O (1-9): "+bcolors.ENDC))
            if(board[userPos-1] != 0):
                print(bcolors.WARNING+"Position occupied. Please choose a different position"+bcolors.ENDC)
                continue

            board = makeMove(board, -1, userPos-1) 
            printBoard(board, reverse)


    
    if(gameStatus(board) != 0):
        if(gameStatus(board) == 1):
            print(bcolors.BOLD+'Computer has won. Better luck next time!'+bcolors.ENDC)
        else:
            print(bcolors.BOLD+'Congratulations! You have won!'+bcolors.ENDC)
    elif(0 not in board):
        print('Draw!')
        