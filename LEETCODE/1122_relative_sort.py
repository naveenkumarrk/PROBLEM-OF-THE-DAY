from collections import defaultdict

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr2_set = set(arr2)
arr1_count =  defaultdict(int)
end = []

for n in arr1:
    if n not in arr2_set:
        end.append(n)
    arr1_count[n]+=1
end.sort()

res = []
for n in arr2:
    for _ in range(arr1_count[n]):
        res.append(n)
print(res+end)

# Output: [2,2,2,1,4,3,3,9,6,7,19]



# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         hash_map = {}
#         for i in range(len(arr2)):
#             hash_map[arr2[i]] = i
        
#         for: i in range (len(arr1))
#             if arr1[i] not in hash_map:
#                 hash_map[arr1[i]] = 1000 + arr1[i]
#         arr1.sort(key = lambda x: hash_map[x])
#         return arr1


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         d  = {v:i for i, v in enumerate(arr2)}
#         return sorted(arr1, key = lambda x:d.get(x,len(arr2)+x))