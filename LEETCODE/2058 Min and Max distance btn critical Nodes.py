# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        self.head = None
        

    def append(self,val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end = "->")
            temp = temp.next
        print("None")
    
    def nodesBetweenCriticalPoints(self, head):
        def critical_point(curr, prev, nxt):
            return (
                prev.val > curr.val < nxt.val or
                prev.val < curr.val > nxt.val
            )
        
        prev, curr = head, head.next
        nxt =  curr. next

        min_dist, max_dist = float('inf'), float('-inf')
        prev_crit_idx = 0 
        first_crit_idx = 0 
        i = 1

        while nxt:
            if critical_point(prev, curr,nxt ):
                    if first_crit_idx:
                        max_dist = i - first_crit_idx
                        min_dist = min(
                            min_dist, 
                            i - prev_crit_idx
                        )
                    else:
                        first_crit_idx = i
                    prev_crit_idx = i

            prev, curr, nxt = curr, nxt, nxt.next
            i+=1

        if min_dist == float('inf'):
            min_dist = -1

        return [min_dist, max_dist]

        
obj = Solution()
arr = [5,3,1,2,5,1,2]
for i in range(len(arr)):
    obj.append(arr[i])
obj.display()
obj.nodesBetweenCriticalPoints(obj)