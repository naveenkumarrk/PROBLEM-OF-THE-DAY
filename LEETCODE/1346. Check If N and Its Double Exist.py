class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False


# class Solution:
#     def checkIfExist(self, nums: List[int]) -> bool:
        
#         mp={}

#         for i in range(len(nums)):
#             if nums[i]*2 in mp or nums[i]/2 in mp:
#                 return True
                

#             else:
#                 mp[nums[i]]=1+mp.get(nums[i],0)
#         return False
                