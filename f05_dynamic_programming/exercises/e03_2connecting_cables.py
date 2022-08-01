cables = [int(x) for x in input().split()]
size = len(cables) + 1
positions = [x for x in range(1, size)]

lcs = []
for _ in range(size):
    lcs.append([0] * size)

for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == positions[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            left = lcs[row][col - 1]
            up = lcs[row - 1][col]
            lcs[row][col] = max(up, left)

print(f"Maximum pairs connected: {lcs[size - 1][size - 1]}")
