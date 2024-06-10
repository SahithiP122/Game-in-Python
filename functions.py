def printBoard(board):
    for i in [0,3,6]:
        print(board[i],'',board[i+1],'',board[i+2],' | ',i+1,'',i+2,'',i+3)
def isValid(board,c):
    if (c<=8 and c>=0):
        if board[c] == '+':
            return True
    return False
def horizontalCheck(board):
    for i in [0,9,18]:
        if (board[i//3] == board[(i//3)+1] == board[(i//3)+2] != '+'):
            return True
    return False
def verticalCheck(board):
    for i in range(3):
        if (board[i] == board[3+i] == board[6+i] != '+'):
            return True
    return False
def diagonalCheck(board):
    c1 = (board[0] == board[4] == board[8] != '+')
    c2 = (board[2] == board[4] == board[6] != '+')
    return c1 or c2
def gameResult(board):
    if (horizontalCheck(board) or verticalCheck(board) or diagonalCheck(board)):
        return 1 # Win
    elif '+' not in board:
        return 0 # Tie
    else:
        return -1 # Play
def minimax(board,player):
    if player == 1:
        if gameResult(board) == 1:
            return -10
        elif gameResult(board) == 0:
            return 0
        else:
            maxScore,score = -1000,-1000
            for i in range(9):
                if board[i] == '+':
                    board[i] = 'X'
                    score = minimax(board,2)
                    board[i] = '+'
                    maxScore = max(maxScore,score)
            return maxScore
    else:
        if gameResult(board) == 1:
            return 10
        elif gameResult(board) == 0:
            return 0
        else:
            minScore,score = 1000,1000
            for i in range(9):
                if board[i] == '+':
                    board[i] = 'O'
                    score = minimax(board,1)
                    board[i] = '+'
                    minScore = min(minScore,score)
            return minScore
def bestMove(board,player):
    best = -1
    if player == 1:
        maxScore,score = -1000,-1000
        for i in range(9):
            if board[i] == '+':
                board[i] = 'X'
                score = minimax(board,2)
                board[i] = '+'
                if score > maxScore:
                    maxScore = score
                    best = i
    else:
        minScore,score = 1000,1000
        for i in range(9):
            if board[i] == '+':
                board[i] = 'O'
                score = minimax(board,1)
                board[i] = '+'
                if score < minScore:
                    minScore = score
                    best = i
    return best