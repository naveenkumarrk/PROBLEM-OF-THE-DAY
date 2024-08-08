mat = [[1, 2, 3, 4], 
       [5, 6, 7, 8], 
       [9, 10, 11, 12], 
       [13, 14, 15,16]]

top, bottom = 0, len(mat)
left , right = 0, len(mat[0])

res = []

while left < right and top < bottom:
    for i in range(left, right):
        res.append(mat[top][i])
    top += 1

    for i in range(top, bottom):
        res.append(mat[i][right-1])
    right -= 1

    if not left < right and top < bottom:
        break

    for i in range(right-1, left-1, -1):
        res.append(mat[bottom-1][i])
    bottom -= 1

    for i in range(bottom -1, top -1, -1):
        res.append(mat[i][left])
    left += 1

print(res)