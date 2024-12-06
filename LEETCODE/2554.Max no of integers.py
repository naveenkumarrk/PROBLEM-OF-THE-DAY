class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        chosen = []
        ban = set(banned)

        for i in range(1, n+1):
            if i not in ban:
                chosen.append(i)
                if sum(chosen) > maxSum:
                    chosen.pop()
        return len(chosen)

        
        # efficient one
        # ans = 0
        # temp = 0
        # banned = set(banned)
        # for i in range(1, n + 1):
        #     if temp >= maxSum or temp + i > maxSum: break
        #     elif i not in banned:
        #         temp += i
        #         ans += 1
        # return ans