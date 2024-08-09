# grid = [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]

# n = len(grid)
# m = len(grid[0])
# i, j = 0, 0
# while i <= m and j != m - 1  


grid = [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

rows = len(grid)
cols = len(grid[0])
res = 0

def magic( r, c):
    # 1 - 9
    value = set()
    for i in range(r, r+3):
        for j in range(c, c+3):
            if grid[i][j] in value or not (0< r < 10 and 0 < c < 10):
                return 0
            value.add(grid[i][j])
    # rows sum 

    for i in range(r, r+3):
        if sum(grid[i][c:c+3]) != 15:
            return 0 
    
    # cols sum 

    for i in range(c, c+3):
        if (grid[r][i] + grid[r+1][i] + grid[r+2][i]) != 15:
            return 0

    # diagnols

    if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or 
        grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]  != 15):
        return 0
    
    return 1
 
for i in range(rows-2):
    for j in range(cols-2):
        res += magic(i, j)

print(res)