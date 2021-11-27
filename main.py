# GLOBAL VARIABLES
# Main state of the board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Indicates which player is to play next
turn = "X"


def main():
    # We start the game here
    start_play = input("Would you like to play Tic Tac Toe? (Y / N) : ")
    expected = ["Y", "N", "y", "n"]

    if start_play not in expected:
        print("This is not a valid choice!")
        start()
    else:
        if start_play == "Y":
            display_board()
            take_turn()
        else:
            exit()


def display_board():
    # Displays the Tic Tac Toe board in it's current state
    line = ""

    for i in range(len(board)):
        for j in range(len(board[i])):
            line = line + board[i][j]

            if j < len(board[i]) - 1:
                line = line + " | "

            if j == len(board[i]) - 1:
                print(line)

                if i < len(board) - 1:
                    print("---------")

                line = ""


def take_turn():
    # Asks the current player where he wants to play his move, places the move on the board, then refreshes the board
    global turn
    move_line = "WRONG"
    move_column = "WRONG"
    expected = ["0", "1", "2"]

    while move_line not in expected:
        move_line = input("Player {}, please choose the line in which you want to play your move "
                          "(0, 1, 2) : ".format(turn))

        if move_line not in expected:
            print("This is not a valid choice!")
    move_line = int(move_line)

    while move_column not in expected :
        move_column = input("Good! Now, please choose the column in which you want to play your move (0, 1, 2) : ")

        if move_column not in expected:
            print("This is not a valid choice!")
    move_column = int(move_column)

    board[move_line][move_column] = "{}".format(turn)

    check_win()
    display_board()

    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    take_turn()


def check_win():
    # Checks if there's a horizontal win
    for i in range(len(board)):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            win("X")
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            win("O")

    # Checks if there's a vertical win
    for i in range(len(board)):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            win("X")
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            win("O")

    # Checks if there's a horizontal win
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        win("X")
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        win("X")
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        win("O")
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        win("O")

    # Checks if the game if is a tie
    istie = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                istie = False

    if istie:
        tie()


def win(winning_player):
    print("Player {} has won!".format(turn))
    new_game()


def tie():
    print("The game is a tie!")
    new_game()


def new_game():
    global board
    decision = input("Would you like to play again? (Y / N) : ")
    expected = ["Y", "N", "y", "n"]

    if decision not in expected:
        print("This is not a valid choice!")
        new_game()
    else:
        if decision == "Y":
            board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            display_board()
            take_turn()
        else:
            exit()




if __name__ == "__main__":
    main()
