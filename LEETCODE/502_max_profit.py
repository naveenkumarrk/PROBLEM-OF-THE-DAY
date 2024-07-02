import heapq
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

def max_capital(k,w,profits,capital):
    maxProfit = []
    minCapital = [(c,p) for c, p in zip(capital, profits)]
    heapq.heapify(minCapital)

    for i in range(k):

        while minCapital and minCapital[0][0] <=w:
            c, p = heapq.heappop(minCapital)
            heapq.heappush(maxProfit, -1 * p)
        if not maxProfit:
            break
        w+= -1 * heapq.heappop(maxProfit)
    return w

max_capital(k,w,profits,capital)



# fucking weird code for more optimisation

# import heapq as heap
# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         if k ==100000 and w == 100000:
#             if profits[0] == 8013:
#                 return 595057
#             return 1000100000

#         if w == 1000000000:
#             return 2000000000
#         minHeap = []
#         maxHeap = []
#         for i in range(len(capital)):
#             heap.heappush(minHeap, (capital[i], profits[i]))
        
#         for i in range(k):
#             while minHeap and minHeap[0][0] <= w:
#                 cap, prof = heap.heappop(minHeap)
#                 heap.heappush(maxHeap, (-prof, cap))
#             if not maxHeap:
#                 break
#             w -= heap.heappop(maxHeap)[0]
#         return w
