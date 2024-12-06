#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        h_cnt = 0
        citations.sort(reverse = True)
        for i, cites in enumerate(citations):
            if cites >= i + 1:
                h_cnt += 1
            else:
                break
            
        return h_cnt