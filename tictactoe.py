def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")

def check_winner(board, player):
    for row in board:
        if all(c == player for c in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[r][c] != " " for r in range(3) for c in range(3))

def main():
    board = [[" "] * 3 for _ in range(3)]
    current = "X"

    print("Tic Tac Toe")
    print("Enter row and column (1-3), e.g. '2 3'\n")

    while True:
        print_board(board)
        print(f"\nPlayer {current}'s turn")
        try:
            row, col = map(int, input("Row Col: ").split())
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Out of range. Use 1-3.\n")
                continue
            if board[row - 1][col - 1] != " ":
                print("Cell taken. Try again.\n")
                continue
        except ValueError:
            print("Invalid input. Enter two numbers like '1 2'\n")
            continue

        board[row - 1][col - 1] = current

        if check_winner(board, current):
            print_board(board)
            print(f"\nPlayer {current} wins!")
            break
        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
