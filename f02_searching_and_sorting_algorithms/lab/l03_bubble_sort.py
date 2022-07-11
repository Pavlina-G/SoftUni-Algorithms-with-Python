def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            previous_num = nums[j - 1]
            current_num = nums[j]
            if previous_num > current_num:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


nums = [int(x) for x in input().split()]
sorted_nums = bubble_sort(nums)
print(*sorted_nums, sep=' ')
