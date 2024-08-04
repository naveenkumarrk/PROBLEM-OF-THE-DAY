# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return Counter(target) == Counter(arr)


with open("user.out", "w") as f:
    for target, arr in zip(map(loads, stdin), map(loads, stdin)):
        f1 = {}
        f2 = {}

        for num in target:
            if num not in f1:
                f1[num] = 0
            
            f1[num] += 1
        
        for num in arr:
            if num not in f2:
                f2[num] = 0
            
            f2[num] += 1
        
        print(["true", "false"][f1 != f2], file=f)

exit()