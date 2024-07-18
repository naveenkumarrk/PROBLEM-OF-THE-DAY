strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):

    # brute force appraoch

    # res, flag = "" , True
    # if strs == "": return ""
    # else:
    #     length = len(strs[0])
    #     for i in range(length):
    #         curr = strs[0]
    #         for j in range(1,len(strs)):
    #             if i >= len(strs[j]) or curr[i] != strs[j][i]:
    #                 flag = False
    #                 break
    #         if flag:
    #             res += curr[i]
    # return res

    # optimized one

    # if strs == "":
    #     return ""
    # else:
    #     for i in range(len(strs)):
    #         base = strs[0][i]
    #         for j in range(len(strs)):
    #             if i == len(strs[j]) or base != strs[j][i]:
    #                 return strs[0][0:i]
    #     return strs[0]
    
    p=strs[0]
    for s in strs[1:]:
        while not s.startswith(p):
            p=p[:-1]
            if not p:
                return ""
    return p