# rowSum = [3,8]
# colSum = [4,7]
# def restoreMatrix(rowSum,colSum):
#     col_sum = colSum
#     row_sum = rowSum
#     ROWS, COLS = len(row_sum), len(col_sum)
#     mat = [[0]* COLS for _ in range(ROWS)]

#     i, j = 0, 0
#     while i < ROWS and j < COLS:
#         mat[i][j] = min(col_sum[j], row_sum[i])

#         row_sum[i] -= mat[i][j]
#         col_sum[j] -= mat[i][j]

#         if row_sum[i] == 0:
#             i += 1
#         else:
#             j += 1
#     return mat

# res = restoreMatrix(rowSum,colSum)
# print(res)

def isPrime(n):
    if n==0 or n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def nums(n):
    for i in range(1,n+1):
        if isPrime(i):
            print(i)

nums(10)