sentence = "i love eating burger"
searchWord = "burg"

def search():
    words = sentence.split()
    for i, word in enumerate(words, 1):
        if word[:len(searchWord)] ==searchWord:
            return i
    return -1