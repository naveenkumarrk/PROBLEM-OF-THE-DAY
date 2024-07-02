# # class Solution:
# #   def maxDistance(self, position: List[int], m: int) -> int:
# #     position.sort()

# #     l = 1
# #     r = position[-1] - position[0]

# #     def numBalls(force: int) -> int:
# #       balls = 0
# #       prevPosition = -force
# #       for pos in position:
# #         if pos - prevPosition >= force:
# #           balls += 1
# #           prevPosition = pos
# #       return balls

# #     while l < r:
# #       mid = r - (r - l) // 2
# #       if numBalls(mid) >= m:
# #         l = mid
# #       else:
# #         r = mid - 1

# #     return l
  




# # #   class Solution:

# # #     def maxDistance(self, position: List[int], m: int) -> int:

# # #         def check(minmax):
# # #             rem = m - 1
# # #             lim = position[0] + minmax
# # #             for p in position[1:]:
# # #                 if p >= lim:
# # #                     rem -= 1
# # #                     lim = p + minmax
# # #             return rem <= 0

# # #         position.sort()
# # #         if m == 2:
# # #             return position[-1] - position[0]
# # #         low = 1
# # #         high = (position[-1] - position[0]) // (m - 1)
# # #         while low < high:
# # #             mid = (low + high + 1) // 2
# # #             if check(mid):
# # #                 low = mid
# # #             else:
# # #                 high = mid -1
# # #         return low        



# from bisect import bisect_left

# class SegmentTree:
#     def __init__(self, data):
#         self.n = len(data)
#         self.data = data
#         self.tree = [None] * (2 * self.n)
#         self.build()
        
#     def build(self):
#         for i in range(self.n):
#             self.tree[self.n + i] = [self.data[i]]
#         for i in range(self.n - 1, 0, -1):
#             self.tree[i] = sorted(self.tree[2 * i] + self.tree[2 * i + 1])
    
#     def update(self, idx, value):
#         pos = idx + self.n
#         self.tree[pos] = [value]
#         pos //= 2
#         while pos > 0:
#             self.tree[pos] = sorted(self.tree[2 * pos] + self.tree[2 * pos + 1])
#             pos //= 2
    
#     def query(self, left, right, value):
#         left += self.n
#         right += self.n
#         count = 0
#         while left < right:
#             if left % 2:
#                 count += len(self.tree[left]) - bisect_left(self.tree[left], value)
#                 left += 1
#             if right % 2:
#                 right -= 1
#                 count += len(self.tree[right]) - bisect_left(self.tree[right], value)
#             left //= 2
#             right //= 2
#         return count

# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     index = 0
    
#     # Read size of array
#     N = int(data[index])
#     index += 1
    
#     # Read array elements
#     A = list(map(int, data[index:index + N]))
#     index += N
    
#     # Read number of queries
#     Q = int(data[index])
#     index += 1
    
#     # Initialize Segment Tree
#     seg_tree = SegmentTree(A)
    
#     results = []
    
#     for _ in range(Q):
#         query = data[index]
#         if query == '0':
#             a = int(data[index + 1]) - 1
#             b = int(data[index + 2])
#             c = int(data[index + 3])
#             results.append(str(seg_tree.query(a, b, c)))
#             index += 4
#         elif query == '1':
#             a = int(data[index + 1]) - 1
#             b = int(data[index + 2])
#             seg_tree.update(a, b)
#             index += 3
    
#     print('\n'.join(results))

# if __name__ == "__main__":
#     main()

from bisect import bisect_left

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [None] * (2 * self.n)
        self.build()
        
    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = [self.data[i]]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = sorted(self.tree[2 * i] + self.tree[2 * i + 1])
    
    def update(self, idx, value):
        pos = idx + self.n
        self.tree[pos] = [value]
        pos //= 2
        while pos > 0:
            self.tree[pos] = sorted(self.tree[2 * pos] + self.tree[2 * pos + 1])
            pos //= 2
    
    def query(self, left, right, value):
        left += self.n
        right += self.n
        count = 0
        while left < right:
            if left % 2:
                count += len(self.tree[left]) - bisect_left(self.tree[left], value)
                left += 1
            if right % 2:
                right -= 1
                count += len(self.tree[right]) - bisect_left(self.tree[right], value)
            left //= 2
            right //= 2
        return count

def main():
    data = [
        '5',
        '12345',
        '3',
        '0 1 5 10',
        '1 2 20',
        '0 3 1 10'
    ]
    
    index = 0
    
    # Read size of array
    N = int(data[index])
    index += 1
    
    # Read array elements
    A = list(map(int, data[index:index + N]))
    index += N
    
    # Read number of queries
    Q = int(data[index])
    index += 1
    
    # Initialize Segment Tree
    seg_tree = SegmentTree(A)
    
    results = []
    
    for _ in range(Q):
        query = data[index].split()
        if query[0] == '0':
            a = int(query[1]) - 1
            b = int(query[2])
            c = int(query[3])
            results.append(str(seg_tree.query(a, b, c)))
            index += 1
        elif query[0] == '1':
            a = int(query[1]) - 1
            b = int(query[2])
            seg_tree.update(a, b)
            index += 1
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
