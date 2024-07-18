def two_sum(nums, target):
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    # return []
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
    return []

res = two_sum([5,4,7,2], 7)
print(res)