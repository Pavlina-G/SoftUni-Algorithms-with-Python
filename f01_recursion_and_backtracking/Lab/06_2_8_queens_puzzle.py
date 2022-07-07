def is_safe(board, row, col):
    for r in range(row):
        if board[r][col] == '*':  # checking columns up to the current row
            return False

    (r, c) = (row, col)
    while r >= 0 and c >= 0:
        if board[r][c] == '*':  # checking left diagonal up to the current row
            return False
        r = r - 1
        c = c - 1

    (r, c) = (row, col)
    while r >= 0 and c < len(board):
        if board[r][c] == '*':  # checking right diagonal up to the current row
            return False
        r = r - 1
        c = c + 1

    return True


def print_board(board):
    for row in board:
        print(*row, sep=' ')
    print()


def put_queens(board, row):
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = '*'  # place queen
            put_queens(board, row + 1)  # recursive call
            board[row][col] = '-'  # backtrack and remove the queen from the current square


n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]
start_row = 0
put_queens(board, start_row)
