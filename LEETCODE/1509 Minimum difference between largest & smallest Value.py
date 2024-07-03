import heapq

nums = [6,6,0,1,1,4,6]

def min_diff(nums):
    # nums.sort()
    if len(nums) <= 4:
        return 0
    
    max_four = sorted(heapq.nlargest(4,nums))
    min_four = sorted(heapq.nsmallest(4,nums))

    res = float('inf') 

    for i in range(4):
        res = min(
            res, 
            max_four[i] - min_four[i]
        )


    # for l in range(4):
    #     r = len(nums) - 4 + l
    #     res = min(
    #         res, 
    #         nums[r] - nums[l]
    #     )


    return res

result = min_diff(nums)
print(result)