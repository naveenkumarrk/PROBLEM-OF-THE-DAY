class Solution:
    def insert(self, alist, index, n):
        #code here
        j = index
        while j > 0 and alist[j-1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j - 1]
            j -= 1
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            self.insert(alist,i, n)
        return alist