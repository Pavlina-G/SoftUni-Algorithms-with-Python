class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def cell_is_not_valid(row, col, matrix):
    return row not in range(len(matrix)) or col not in range(len(matrix[0]))


def find_area(row, col, matrix):
    if cell_is_not_valid(row, col, matrix):
        return 0
    if matrix[row][col] != '-':
        return 0
    matrix[row][col] = 'v'

    result = 1
    result += find_area(row - 1, col, matrix)
    result += find_area(row + 1, col, matrix)
    result += find_area(row, col - 1, matrix)
    result += find_area(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]

areas = []
for row in range(rows):
    for col in range(cols):
        size = find_area(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for index, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}')
