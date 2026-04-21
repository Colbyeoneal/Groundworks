def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers.")

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    main()