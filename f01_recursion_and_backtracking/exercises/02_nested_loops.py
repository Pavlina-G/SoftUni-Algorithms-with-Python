def recursive_nested_loop(loops, idx):
    if idx == len(loops):
        print(*loops, sep=' ')
        return
    for num in range(1, n + 1):
        loops[idx] = num
        recursive_nested_loop(loops, idx + 1)


n = int(input())
loops = [None] * n
index = 0
recursive_nested_loop(loops, index)