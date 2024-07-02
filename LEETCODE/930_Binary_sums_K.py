# Prefix and dict properties

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans ,prefix_sum = 0, 0
        freq = {0:1}

        for ele in nums:
            prefix_sum += ele
            if (prefix_sum - goal) in freq:
                ans += freq[prefix_sum - goal]
            if prefix_sum in freq:
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1
        return ans
    

# Sliding Window and Prefix Properties


# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         def inclu_exclu_prin(x):
#             res = 0
#             curr = l = 0
#             if x <0:
#                 return 0
#             for r in range(len(nums)):
#                 curr += nums[r]
#                 while curr > x: 
#                     curr -= nums[l]
#                     l+=1
#                 res += (r - l + 1)
#             return res

#         return inclu_exclu_prin(goal) - inclu_exclu_prin(goal-1)