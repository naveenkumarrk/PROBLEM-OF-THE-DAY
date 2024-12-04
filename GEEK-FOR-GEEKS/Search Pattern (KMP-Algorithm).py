# brute force approach

# class Solution:
#     def search(self, pat, txt):
#         # code here
#         res = []
#         for i in range(len(txt)):
#             j = len(pat)
#             if txt[i:i+j] == pat:
#                res.append(i)
#         return res
    
# Knuth-Morris-Pratt (KMP algorithm)

class Solution:
    def search(self, pat, txt):
        # code here
        def get_lps(pat):
            lps = [0] * len(pat)
            
            prevLps, i = 0, 1
            
            while i < len(pat):
                if pat[i] == pat[prevLps]:
                    lps[i] =prevLps + 1
                    prevLps += 1
                    i += 1
                
                else:
                    if prevLps == 0:
                        lps[i] = 0
                        i += 1
                    else: 
                        prevLps = lps[prevLps -1]
            return lps
        
        # KMP algorithm
        indices = []
        n, m = len(txt), len(pat)
        lps = get_lps(pat)
        i = j = 0
        
        while i < n:
            if txt[i] == pat[j]:
               i += 1
               j += 1
            
            if j == m:
                indices.append(i-j)
                j = lps[j-1]
            
            elif i < n and txt[i] != pat[j]:
                if j == 0:
                    i += 1
                    
                else:
                    j = lps[j -1]
            
            
        return indices
            
        
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends
