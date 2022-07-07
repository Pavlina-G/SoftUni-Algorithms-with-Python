def is_valid(row, col, lab):
    return row in range(len(lab)) and col in range(len(lab[0]))


def find_all_paths(row, col, lab, direction, path):
    if not is_valid(row, col, lab):
        return

    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row, col + 1, lab, 'R', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        lab[row][col] = '-'

    path.pop()


rows = int(input())
columns = int(input())

labyrinth = []

for row in range(rows):
    labyrinth.append(list(input()))

start_row = 0
start_col = 0
find_all_paths(start_row, start_col, labyrinth, '', [])
