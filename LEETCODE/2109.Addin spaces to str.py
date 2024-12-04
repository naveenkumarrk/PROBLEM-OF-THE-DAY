class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # s = list(s)
        # res = ''
        # for i in range(len(s)):
        #     if i in spaces:
        #         res += ' '
        #     res += s[i]
        # return res

        res = []
        space_index = 0

        for i, char in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                res.append(' ')
                space_index += 1
            res.append(char)
        return ''.join(res)
