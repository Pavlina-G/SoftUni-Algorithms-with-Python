def sum_numbers(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + sum_numbers(nums, idx+1)

numbers = [int(x) for x in input().split()]
index = 0
print(sum_numbers(numbers, index))
