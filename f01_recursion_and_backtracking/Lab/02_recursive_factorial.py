def rec_fact(n):
    if n == 1:  #  n <= 1
        return n #  return 1
    return n * rec_fact(n - 1)


n = int(input())
print(rec_fact(n))
