words = ["bella","label","roller"]

'''Cooler solution'''
# def common_chars(words):
#     res = []
#     chars = set(words[0])
    
#     for char in chars:
#         freq = min([word.count(char) for word in words])
#         res += freq * [char]
        
#     return res
# print(common_chars(words))
from collections import Counter


def commonChars(words):
    common_words = Counter(words[0])
    res = []
    for word in words[1:]:
        curr_wrd_count = Counter(word)
        for char in common_words:
            common_words[char] = min(common_words[char], curr_wrd_count[char])
    for char , freq in common_words.items():
        res.extend([char] * freq)
    return res 

print(commonChars(words))