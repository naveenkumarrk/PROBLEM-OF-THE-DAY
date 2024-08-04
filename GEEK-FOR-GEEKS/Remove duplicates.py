

def removeDuplicates(text):
    # ls = []
    # freq = {}

    # for i in text:
    #     if i in freq:
    #         freq[i] += 1
    #         continue
    #     else:
    #         freq[i] = 1
    #         ls.append(i)

    # return "".join(ls)

# ------------easier one ---------------------
    res = ""
    for i in text:
        if i not in res:
            res += i
    return res

res = removeDuplicates("ertyuioerterty")
print(res)