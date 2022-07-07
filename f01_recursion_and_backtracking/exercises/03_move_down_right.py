def not_valid(row, col, grid):
    return row not in range(len(grid)) or col not in range(len(grid[0]))


def find_exit(grid, row, col, path, exit):
    if not_valid(row, col, grid):
        return

    exit_row, exit_col = exit

    if row == exit_row and col == exit_col:
        path.append(1)
    else:
        find_exit(grid, row, col + 1, path, exit)
        find_exit(grid, row + 1, col, path, exit)

    return path


m = int(input())
n = int(input())
grid = [[None] * n for row in range(m)]
start_row = 0
start_col = 0
exit = (m - 1, n - 1)
all_paths = (find_exit(grid, start_row, start_col, [], exit))
print(len(all_paths))
