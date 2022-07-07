# def reverse_array(array):
#     if not array:
#         return []
#     return [array.pop()] + reverse_array(array)
#
#
# array = [int(x) for x in input().split()]
# print(*reverse_array(array))

# ---------------------------------------------

def reverse_array(array, index):
    if index == -(len(array)):
        return array[index]
    return f'{array[index]} {reverse_array(array, index - 1)}'


array = [int(x) for x in input().split()]
start_index = -1
print(reverse_array(array, start_index))