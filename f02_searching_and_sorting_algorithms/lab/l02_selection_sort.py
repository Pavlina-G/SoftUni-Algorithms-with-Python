def selection_sort(nums):
    for i in range(len(nums)):
        min_num = nums[i]
        min_index = i
        for j in range(i+1, len(nums)):
            current_num = nums[j]
            if current_num < min_num:
                min_num = current_num
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    print(*nums,sep=' ')

nums = [int(x) for x in input().split()]
selection_sort(nums)
