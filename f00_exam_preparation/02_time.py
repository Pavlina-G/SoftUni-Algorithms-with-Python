from collections import deque


def create_dp_matrix(rows, cols):
    matrix = []
    [matrix.append([0] * cols) for _ in range(rows)]
    return matrix


def find_count_lcs(dp, rows, cols, first, second):
    for row in range(1, rows):
        for col in range(1, cols):
            if first[row - 1] == second[col - 1]:
                # prev = dp[row-1][col-1]
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                # up = dp[row-1][col]
                # left = dp[row][col-1]
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp[rows - 1][cols - 1]


def find_lcs_numbers(dp, rows, cols, first, second):
    row = rows - 1
    col = cols - 1
    result = deque()

    while row >= 0 and col >= 0:
        if first[row - 1] == second[col - 1]:
            result.appendleft(first[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1
    return result


first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1

dp = create_dp_matrix(rows, cols)
count = find_count_lcs(dp, rows, cols, first, second)
lcs_nums = find_lcs_numbers(dp, rows, cols, first, second)

print(' '.join(lcs_nums))
print(count)
