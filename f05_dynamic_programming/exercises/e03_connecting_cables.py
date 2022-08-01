from collections import deque

cables = [int(x) for x in input().split()]
size = [0] * len(cables)
parent = [None] * len(cables)

best_size = 1
best_idx = 0

for current_idx in range(1, len(cables)):
    current_cable = cables[current_idx]
    current_best_size = 1
    current_parent = None

    for prev_idx in range(current_idx - 1, -1, -1):
        prev_cable = cables[prev_idx]

        if prev_cable >= current_cable:
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
    result.appendleft(cables[index])
    index = parent[index]

print(f"Maximum pairs connected: {len(result)}")