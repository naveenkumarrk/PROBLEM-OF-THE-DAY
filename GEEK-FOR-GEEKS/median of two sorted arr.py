arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]

def sum_of_middle_elements(arr1, arr2):
    # code here
    nums = arr1 + arr2
    nums = sorted(nums)
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    else:
        return nums[n//2] + nums[n//2 - 1]
        
p = sum_of_middle_elements(arr1, arr2)
print(p)