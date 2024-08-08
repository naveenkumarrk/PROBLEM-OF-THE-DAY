# s = "abababd"

# def maxHappyPreSuf(s):
#     preFreq = {}
#     sufFreq = {}
#     maxHappy = ''
#     for i in range(1,len(s)):
#         preFreq[s[:i]] = preFreq.get(s[:i], 0) + 1

#     for i in range(len(s)-1, 0, -1):
#         sufFreq[s[i:]] = sufFreq.get(s[i:], 0) + 1

#     for key, val in preFreq.items():
#         if key in sufFreq:
#             if len(key) > len(maxHappy):
#                 maxHappy = key 

#     return maxHappy

# print(maxHappyPreSuf(s))



# n = 6
# cnt = n
# for i in range(n, 0,-1):
#     for j in range(i,n+1):
#         print(j, end = "")
#     cnt -= 1
#     for k in range(cnt):
#         print(n, end = "")
#     print()

# s = 'zzdccffff'
# def noRepeat(s):
#     res = ''
#     i= 1
#     while i <= len(s):
#         if s[i-1] == s[i]:
#             res += s[i-1] + '*'
#             i += 2
#         else:
#             res += 2*s[i-1]
#             i += 2


#     return res

# print(noRepeat(s))
            

        

def pattern(n):
    total = []
    for i in range(2, n+2):
        if total:
            rem = total.pop()
            total.append(i**2 - rem)
        else:
            total.append(i**2)
    print(*total)

pattern(6)