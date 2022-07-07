def draw_figure(n, ch='*'):
    if n == 0:
        return

    print(ch * n) # Pre-actions (before calling the recursion)
    draw_figure(n - 1) # Recursive calls (step-in)
    ch = '#'
    print(ch * n) # Post-actions (after returning from recursion)


n = int(input())
draw_figure(n)

# def draw_figure(n):
#     if n == 0:
#         return
#     print('*' * n)
#     draw_figure(n - 1)
#     print('#' * n)
#
#
# n = int(input())
# draw_figure(n)