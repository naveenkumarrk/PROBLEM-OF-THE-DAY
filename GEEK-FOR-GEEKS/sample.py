n= 3
arr = [35, 9, 1]
cube = [1]
cnt = 0
i = 1
limit = max(arr)
while i < limit:
    i += 1
    cSum = i ** 3 + limit **3
    cube.append(cSum)
    limit -= 1 

print(cube)
