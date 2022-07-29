from collections import deque

nums = [int(x) for x in input().split()]
size = [0] * len(nums)
parent = [None] * len(nums)

best_size = 1
best_idx = 0

for current_idx in range(1, len(nums)):
    current_num = nums[current_idx]
    current_best_size = 1
    current_parent = None

    for prev_idx in range(current_idx - 1, -1, -1):
        prev_num = nums[prev_idx]

        if prev_num >= current_num:
            continue

        if size[prev_idx] + 1 >= current_best_size:
            current_best_size = size[prev_idx] + 1
            current_parent = prev_idx

    size[current_idx] = current_best_size
    parent[current_idx] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current_idx

result = deque()
index = best_idx

while index != None:
    result.appendleft(nums[index])
    index = parent[index]

print(*result, sep=' ')
