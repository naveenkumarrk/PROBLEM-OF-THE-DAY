class Solution:
    def Maximize(self, a): 
        # Complete the function
        MOD = (10 **9 + 7)
        a.sort()
        res = 0
        for i in range(len(a)):
            res += (a[i] * i % MOD)
        return res
obj = Solution()
a = [5, 3, 2, 4, 1]
res = obj.Maximize(a)
print(res)
