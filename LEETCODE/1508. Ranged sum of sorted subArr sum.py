import heapq

nums  = [1,2,3,4]
left = 1
right = 5
n = 4

def rangedSubSum(nums, n, left, right):
    MOD = (10 ** 9 + 7)
    minHeap = [(n, i) for i, n in enumerate(nums)]
    # print(minHeap)

    heapq.heapify(minHeap)

    res = 0
    for i in range(right):
        num , index = heapq.heappop(minHeap)
        if i >= left-1:
            res = (res + num) % MOD
        if index + 1 < n:
            next_pair = (num + nums[index+1], index + 1)
            heapq.heappush(minHeap, next_pair)
    return res

print(rangedSubSum(nums, n, left, right))


rangedSubSum(nums, n, left, right)