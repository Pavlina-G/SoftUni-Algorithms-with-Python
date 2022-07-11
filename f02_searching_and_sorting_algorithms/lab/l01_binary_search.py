def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_element = nums[mid_idx]

        if target == mid_element:
            return mid_idx

        if target < mid_element:
            right = mid_idx - 1
        else:
            left = mid_idx + 1

    return -1


numbers = [int(x) for x in input().split()]
target_num = int(input())
print(binary_search(numbers, target_num))
