# GLOBAL VARIABLES
# Main state of the board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Indicates which player is to play next
turn = "1"


def main():
    # We start the game here
    start_play = input("Would you like to play Tic Tac Toe? (Y / N) : ")
    expected = ["Y", "N", "y", "n"]

    if start_play not in expected:
        print("This is not a valid choice!")
        main()
    else:
        if start_play == "Y" or start_play == "y":
            display_board()
            take_turn()
        else:
            exit()


def display_board():
    # Displays the Tic Tac Toe board in it's current state

    print("\n" * 100)

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
    move_legal = True
    move_line = None
    move_column = None
    expected = ["1", "2", "3"]

    while move_legal:
        while move_line not in expected:
            move_line = input("Player {}, please choose the line in which you want to play your move "
                              "(1 / 2 / 3) : ".format(turn))

            if move_line not in expected:
                print("This is not a valid choice!")
        move_line = int(move_line)

        while move_column not in expected:
            move_column = input(
                "Good! Now, please choose the column in which you want to play your move (1 / 2 / 3) : ")

            if move_column not in expected:
                print("This is not a valid choice!")
        move_column = int(move_column)

        if board[move_line - 1][move_column - 1] != " ":
            print("You cannot play a move in a square that's already used!")
            continue
        else:
            break

    if turn == "1":
        board[move_line - 1][move_column - 1] = "X"
    else:
        board[move_line - 1][move_column - 1] = "O"

    check_win()
    check_tie()
    display_board()

    if turn == "1":
        turn = "2"
    else:
        turn = "1"
    take_turn()


def check_win():
    # Checks if there's a horizontal win
    for i in range(len(board)):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            win("1")
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            win("2")

    # Checks if there's a vertical win
    for i in range(len(board)):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            win("1")
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            win("2")

    # Checks if there's a horizontal win
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        win("1")
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        win("1")
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        win("2")
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        win("2")


def check_tie():
    # Checks if the game if is a tie
    istie = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                istie = False

    if istie:
        tie()


def win(winning_player):
    display_board()
    print("Player {} has won!".format(turn))
    new_game()


def tie():
    display_board()
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
