def not_valid(row, col, matrix):
    return row not in range(len(matrix)) or col not in range(len(matrix[0]))


def dfs(parent, row, col, matrix, visited):
    if not_valid(row, col, matrix):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for row in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 0
        areas[key] += 1

print(f"Areas: {sum(areas.values())}")

for area, value in sorted(areas.items()):
    print(f"Letter '{area}' -> {value}")
