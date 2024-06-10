import sys
from functions import *

line = "------------------------------------"

def playGame():
    print("---Welcome to Tic-Tac-Toe---")
    print("Position Numbers are shown beside the game board")
    board = ['+' for _ in range(9)]
    printBoard(board)
    print(line)

    m = {'AI' : 1, 'HUMAN' : 2}

    p1 = (input("Select Player 1 - (HUMAN or AI) : ")).upper()
    while p1 != "AI" and p1 != "HUMAN":
        print("Invalid Player Type!")
        p1 = (input("Select Player 1 - (HUMAN or AI) : ")).upper()

    p2 = (input("Select Player 2 - (HUMAN or AI) : ")).upper()
    while p2 != "AI" and p2 != "HUMAN":
        print("Invalid Player Type!")
        p2 = (input("Select Player 2 - (HUMAN or AI) : ")).upper()

    print(line)
    print(f"Player1({p1}) - X | Player2({p2}) - O")
    print(line)

    counter = 0

    while True:
        if counter%2 == 0:
            print("Turn : Player1")
            if m[p1] == 2:
                while True:
                    c1 = int(input("Player1 Choice : "))
                    if isValid(board,c1-1):
                        break
                    print("Invalid Entry!")
                board[c1-1] = 'X'
            else:
                b1 = bestMove(board,1)
                board[b1] = 'X'
            

        else:
            print("Turn : Player2")
            if m[p2] == 2:
                while True:
                    c2 = int(input("Player2 Choice : "))
                    if isValid(board,c2-1):
                        break
                    print("Invalid Entry!")
                board[c2-1] = 'O'
            else:
                b2 = bestMove(board,2)
                board[b2] = 'O'


        printBoard(board)
        print(line)

        counter += 1

        if gameResult(board) == 1:
            if counter%2 == 0:
                sys.exit("Player2 Won!!")
            else:
                sys.exit("Player1 Won!!")

        if gameResult(board) == 0:
            sys.exit("Game Tie!!")

playGame()