# https://leetcode.com/problems/subarray-sums-divisible-by-k/




class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        c,l=0,0
        
        for i in range(len(nums)):
            c=c+nums[i]
            m=c%k
            if m in d:
                l=l+d[m]
                d[m]+=1
            else:
                d[m]=1
        return l
    
    
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = [0] * k
        table[0] = 1
        s = 0
        count = 0
        for n in nums:
            s += n
            s %= k
            count += table[s]
            table[s] += 1
        return count