s= "abccccdd"

def longest_palin(s):
    dict = {}
    count = 0
    for  x in s:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1
    isOdd = False
    for key, val in dict.items():
        if val% 2 == 0:
            count+=val
        else:
            count += val-1
            isOdd = True
    return count+1 if isOdd else count

print(longest_palin(s))