
# {Brute Force O(n^3)}
# -----------------------------------------------------------------------------------------------


# nums = [8,2,4,7]
# limit = 4
# ls = []
# valid = []
# count = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)+1):
#         ls.append(nums[i:j])

# for ele in ls:
#     if max(ele) - min(ele) <= limit:
#         valid.append(len(ele))
# valid = set(valid)
# print(max(valid))





# {using index for max and min elements}
# -----------------------------------------------------------------------------------------------

# from collections import deque

# nums = [8,2,4,7]
# limit = 4

# max_len =0
# l ,r =  0,0

# min_q = deque()
# max_q = deque()
# while r < len(nums):

#     while min_q and nums[r] <= nums[min_q[-1]]:
#         min_q.pop()
#     min_q.append(r)

#     while max_q and nums[r] >= nums[max_q[-1]]:
#         max_q.pop()
#     max_q.append(r)

#     while nums[max_q[0]] - nums[min_q[0]] > limit:
#         l+=1
#         while min_q[0] < l:
#             min_q.popleft()

#         if max_q[0] < l:
#             max_q.popleft()

#     max_len = max(max_len, r-l+1)
#     r += 1

# max_len


# {Using actual elements for comparision like max and min}
# -----------------------------------------------------------------------------------------------


# from collections import deque

# nums = [8, 2, 4, 7]
# limit = 4

# max_len = 0
# l, r = 0, 0

# # Initialize the deques outside the while loop
# min_q = deque()
# max_q = deque()

# while r < len(nums):
#     # Maintain min deque (increasing order)
#     while min_q and nums[r] <= nums[min_q[-1]]:
#         min_q.pop()
#     min_q.append(r)

#     # Maintain max deque (decreasing order)
#     while max_q and nums[r] >= nums[max_q[-1]]:
#         max_q.pop()
#     max_q.append(r)

#     # While the current window does not satisfy the condition, shrink the window
#     while nums[max_q[0]] - nums[min_q[0]] > limit:
#         l += 1
#         if min_q[0] < l:
#             min_q.popleft()
#         if max_q[0] < l:
#             max_q.popleft()

#     # Update the maximum length of the window
#     max_len = max(max_len, r - l + 1)
#     r += 1

# print(max_len)



# {Sliding window using inbuild functions }
# -----------------------------------------------------------------------------------------------

# nums = [8,2,4,7]
# limit = 4
