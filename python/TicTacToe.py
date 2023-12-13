board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

    row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
    col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

    if board[row][col] == " ":
        board[row][col] = current_player

        for row in board:
            if all(cell == current_player for cell in row):
                print(" | ".join(row))
                print(f"Player {current_player} wins!")
                exit()

        for col in range(3):
            if all(board[row][col] == current_player for row in range(3)):
                print(f"Player {current_player} wins!")
                exit()

        if all(board[i][i] == current_player for i in range(3)) or all(board[i][2 - i] == current_player for i in range(3)):
            print(f"Player {current_player} wins!")
            exit()

        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            exit()

        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell already taken. Try again.")
