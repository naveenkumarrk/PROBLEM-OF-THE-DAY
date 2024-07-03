# Linked list Node class

class Node :
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def display(self, head):
        while head:
            print(head.data, end = "->")
            head = head.next
        print("None")

    def occurrence(self, head):
        freq = {}
        while head:
            if head.data in freq:
                freq[head.data] += 1
            else:
                freq[head.data] = 1
            head = head.next
        
        res = [key for key,val in freq.items() if val == 1]
        return res

    def occurrences_head(self, head):
        temp = head 
        freq = {}
        #Count frequencies
        while temp:
            freq[temp.data] = freq.get(temp.data, 0) + 1
            temp = temp.next

        dummy = Node(-1)
        new_list = dummy

        temp = head
        while temp:
            if freq[temp.data] == 1:
                new_list.next = Node(temp.data)
                new_list = new_list.next
            temp = temp.next
        
        return dummy.next





head = Node(23)
head.next = Node(28)
head.next.next = Node(28)
head.next.next.next = Node(35)
head.next.next.next.next = Node(49)
head.next.next.next.next.next = Node(49)
head.next.next.next.next.next.next = Node(53)
head.next.next.next.next.next.next.next = Node(53)

obj = Solution()
obj.display(head)
result = obj.occurrence(head)
# print(result)

result1 = obj.occurrences_head(head)
obj.display(result1)
# List = 23->28->28->35->49->49->53->53