def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 5:
            return True

    # Check columns
    for col in range(15):
        if [board[row][col] for row in range(15)].count(player) == 5:
            return True

    # Check diagonals
    for row in range(11):
        for col in range(11):
            if all(board[row + i][col + i] == player for i in range(5)):
                return True
            if all(board[row + i][col + 4 - i] == player for i in range(5)):
                return True

    return False

def is_valid_move(board, row, col):
    return 0 <= row < 15 and 0 <= col < 15 and board[row][col] == "."

def play_gomoku():
    board = [["."]*15 for _ in range(15)]
    current_player = "X"

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0-14): "))
        col = int(input(f"Player {current_player}, enter column (0-14): "))

        if is_valid_move(board, row, col):
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif all(cell != "." for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_gomoku()

