class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        curr = count = 0
        freq = {0:1}
        for ele in nums:
            curr += ele

            if curr - k in freq:
                count += freq[curr - k]
            if curr in freq:
                freq[curr] += 1 
            else:
                freq[curr] = 1
        return count
    

# problem Binary Subarrays and SubArray Sum K is same logic

    # class Solution:
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     def inclu_exclu_prin(x):
    #         res = 0
    #         curr = l = 0
    #         if x <0:
    #             return 0
    #         for r in range(len(nums)):
    #             curr += nums[r]
    #             while curr > x: 
    #                 curr -= nums[l]
    #                 l+=1
    #             res += (r - l + 1)
    #         return res

    #     return inclu_exclu_prin(goal) - inclu_exclu_prin(goal-1)