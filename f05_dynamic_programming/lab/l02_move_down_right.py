from collections import deque

rows = int(input())
columns = int(input())
matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * columns)

# First -> all base solutions
dp[0][0] = matrix[0][0]

for col in range(1, columns):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

# Fill next
for row in range(1, rows):
    for col in range(1, columns):
        up = dp[row - 1][col]
        left = dp[row][col - 1]
        dp[row][col] = matrix[row][col] + max(up, left)

# find path

path = deque()
row = rows - 1
col = columns - 1

while row > 0 and col > 0:
    path.appendleft([row, col])
    if dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

for i in range(row, 0, -1):
    path.appendleft([i, col])
for i in range(col, 0, -1):
    path.appendleft([row, i])
path.appendleft([0, 0])

print(*path)
