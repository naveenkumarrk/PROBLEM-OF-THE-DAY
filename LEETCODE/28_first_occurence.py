haystack = "sadbutsad"
needle = "sad"
def strStr(self, haystack: str, needle: str) -> int:
        # if len(haystack) < len(needle):
        #     return -1
        # for i in range(len(haystack) + 1 - len(needle)):
        #     if haystack[i : i + len(needle)] == needle:
        #         return i
        # return -1
        try:
            return haystack.index(needle)
        except:
            return -1
        
res = strStr(haystack, needle)
print(res)