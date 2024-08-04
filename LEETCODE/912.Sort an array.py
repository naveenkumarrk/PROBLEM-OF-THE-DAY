class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0 , len(nums)-1)
        return nums

    def merge_sort(self, arr: List[int], left: int, right: int):
        if left >= right:
            return
        mid = (left + right) // 2

        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid+1, right)

        self.merge(arr, left, mid, right)
    
    def merge(self, arr: List[int], low: int, mid: int, high: int):
        left_arr : List[int] = arr[low: mid+1]
        right_arr : List[int] = arr[mid +1 : high+1]
        i, j, k = 0, 0, low

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k += 1
        while i < len(left_arr):
            arr[k]= left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k]= right_arr[j]
            j+=1
            k+=1

