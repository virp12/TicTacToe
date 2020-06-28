
"""

TIC TAC TOE

"""

# Creates a function that displays the board every time a change is made.
def create_board(board):
    print("|     |     |     |")
    print("|  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+"  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print("|  "+board[3]+"  |  "+board[4]+"  |  "+board[5]+"  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print("|  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+"  |")
    print("|     |     |     |")
    print("-------------------")


# Allow user to select marker choice and store it in a list.
list1 = []
def select_marker(list1):


    marker = str(input("Player 1, would you like to be 'X' or 'O'? \n").upper())
    if marker == 'X':
        list1.append(marker)
        list1.append('O')
    elif marker == 'O':
        list1.append(marker)
        list1.append('X')


    print(list1)



# Allow Player 1 to choose index number to place marker on board and check for filled positions.
def place_marker_1(board, list1):
    while True:
        position1 = int(input("Player 1, Where would you like to place your marker? (Enter position number 0-8): \n"))


        if board[position1] == list1[0]:
            print("Position filled. Pick a different position.")
        elif board[position1] == list1[1]:
            print("Position filled. Pick a different position.")
        else:
            board[position1] = (list1[0])
            print(create_board(board))
            break


# Allow Player 2 to choose index number to place marker on board and check for filled positions.
def place_marker_2(board, list1):
    while True:
        position2 = int(input("Player 2, Where would you like to place your marker? (Enter position number 0-8): \n"))

        if board[position2] == list1[1]:
            print("Position filled. Pick a different position.")
        elif board[position2] == list1[0]:
            print("Position filled. Pick a different position.")
        else:
            board[position2] = (list1[1])
            print(create_board(board))
            break

# Check if board is full and game is a tie.
def full_board_check(board):
    if " " not in board:
        print('TIE')

# Check if either player won.
def check_win(board, mark):
    return((board[0] == mark and board[1] == mark and board[2] == mark) or
           (board[3] == mark and board[4] == mark and board[5] == mark) or
           (board[6] == mark and board[7] == mark and board[8] == mark) or
           (board[0] == mark and board[3] == mark and board[6] == mark) or
           (board[1] == mark and board[4] == mark and board[7] == mark) or
           (board[2] == mark and board[5] == mark and board[8] == mark) or
           (board[2] == mark and board[4] == mark and board[6] == mark) or
           (board[0] == mark and board[4] == mark and board[8] == mark))


# Main function to run full game.
def main():

    while True:
        print('Welcome to Tic Tac Toe!')
        theBoard = [' '] * 9
        create_board(theBoard)

        select_marker(list1)
        while True:

            place_marker_1(theBoard, list1)

            if check_win(theBoard,list1[0]) == True:
                print('Player 1 won')

                break


            place_marker_2(theBoard,list1)

            if check_win(theBoard,list1[1]) == True:
                print('Player 2 won')

                break

            if full_board_check(theBoard):
                break

        list1.clear()



main()
