arr = ["d","b","c","b","c","a"]
# arr = ['aaa','aa','a']
k = 2
def distinctStr(arr, k):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    for i in arr:
        if freq[i] == 1:
            k -= 1
        if k == 0:
            return i
    return ''

def distinctStrSet(arr, k):
    dis = set()
    dup = set()

    for i in arr:
        if i in dup:
            continue

        if i in dis:
            dis.remove(i)
            dup.add(i)
        else:
            dis.add(i)

    for i in arr:
        if i not in dup:
            k -= 1
         
        if k == 0:
            return i
    
    return ''

c = distinctStrSet(arr, k)
print(c)