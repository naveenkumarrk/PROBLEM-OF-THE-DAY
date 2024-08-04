text =  "the quick brown fox jumps over the lazy dog"
k = 0
def kPangrams(text, k):
    total = 0
    unique = 0
    charMap = [False] * 26
    for char in text:
        if char != " ":
            i = ord(char) - ord('a')
            # print(f"{char}:{i}")
            total += 1
        if not charMap[i]:
            charMap[i] = True
            unique += 1
    print(unique)
    return unique + k >= 26 and total >=  26

res = kPangrams(text, k)
print(res)