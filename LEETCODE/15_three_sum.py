nums = [-1,0,1,2,-1,-4]
nums.sort()
n = len(nums)
res = []

for i in range(n-1):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    left , right = i + 1, n-1
    while left < right:
        temp = nums[i] + nums[left] + nums[right]
        if temp == 0:
            res.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right -1]:
                right -= 1
            left += 1 
            right -= 1
        elif temp < 0:
            left += 1
        else:
            right -= 1
print(res)


# res = []
# for i in range(n-1):
#     for j in range(i+1, n):
#         temp_sum = nums[i] + nums[j]
#         for k in range(len(nums)):
#             if temp_sum + nums[k] == 0:
#                 res.append([nums[i],nums[j], nums[k]])

# print(set(res))