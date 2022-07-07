def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2, 4):
        vector[idx] = num
        gen01(idx + 1, vector)


n = int(input())
vector = [None] * n
index = 0
gen01(index, vector)