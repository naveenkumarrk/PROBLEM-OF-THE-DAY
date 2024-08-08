# class Solution:
#     def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
#         direction = [[0, 1], [1, 0], [0, -1], [0, -1]]
#         r, c = rStart, cStart
#         res = []
#         steps = 1
#         i = 0

#         while len(res) < rows * cols:
#             for _ in range(2):
#                 dr , dc = direction[i]
#                 for _ in range(steps):
#                     if (0 <= r < rows and 0 <= c < cols):
#                         res.append([r,c])
#                     r, c = r + dr, c + dc
#                 i = (i + 1) % 4
#             steps += 2
#         return res
    
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        i,j = rStart, cStart

        diri, dirj = 0, 1 # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and ( -1 < j < cols):
                res.append([i,j])
            
            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res
