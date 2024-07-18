s = "[]}"
def valid_paren(s):
#     for i in range(len(s)-1):
#         if s[i] == '(' and s[i+1] != ')':
#             return False
#         elif s[i] == '[' and s[i+1] != ']':
#             return False
#         elif s[i] == '{}' and s[i+1] != '}':
#             return False
#         else:
#             return True
    stack = []
    mapping = {')' : '(', ']' : '[', '}' : '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
    # while '()' in s or '[]' in s or '{}' in s:
    #     s = s.replace('{}', '')
    #     s = s.replace('[]', '')
    #     s = s.replace('()', '')
    # return s == ''

res = valid_paren(s)
print(res)