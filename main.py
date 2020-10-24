import random
from checkWinner import isWinner
from bot import compInput

board = [' ']*10


def isValidInput(pos):
    if pos > 0 and pos < 11:
        if board[pos] == ' ':
            return True
        else:
            print("Position already occupied!!")
            return False
    else:
        print("Number should be between 1-9!!")
        return False


def gameComplete():
    for i in board[1:]:
        if i == ' ':
            return False
    return True


'''
def compInput():
    pos = []
    for i in range(1, len(board)):
        if board[i] == ' ':
            pos.append(i)
    return random.choice(pos)
'''


def printBoard():
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("\n")


def clearBoard():
    global board
    board = [' ']*10


def main():
    global board
    game = 'y'
    while game.lower() == 'y':
        printBoard()
        in1 = str(input("Do you want to go first, Y/N:"))
        if in1.lower() == 'n':
            board[1] = 'O'
            printBoard()
            print("Bot plays 'O' at pos 1")
        while True:
            u_in = False
            while u_in == False:
                pos = int(input("Enter a pos(1-9):"))
                u_in = isValidInput(pos)

            u_in = False
            board[pos] = 'X'
            printBoard()
            if isWinner(board, 'X'):
                print("Player wins!!")
                break
            else:
                if gameComplete():
                    print("Tie")
                    break
                pos = compInput(board.copy(), 'O')
                board[pos] = 'O'
                print("Bot plays 'O' at pos "+str(pos))
            printBoard()
            if isWinner(board, 'O'):
                print("Bot wins!!")
                break

            if gameComplete():
                print("Tie")
                break
        clearBoard()
        game = str(input("Play a new game Y/N:"))


main()
