
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

    def merge_zeros(self,head):
        temp = head
        ls = []
        total = 0
        while temp:
            if temp.data == 0:
                temp = temp.next
                ls.append(total)
                total = 0
                continue
            else:
                total += temp.data
            temp = temp.next

        dummy = Node(-1)
        new_node = dummy
        for i in range(1, len(ls)):
            new_node.next = Node(ls[i])
            new_node = new_node.next

        return dummy.next
    

    def optimized_zeros(self, head):
        l = head
        r = head.next
        total = 0
        while r:
            if r.data == 0:
                l = l.next
                l.data = total
                total = 0
            else:
                total += r.data
            r = r.next
        l.next = None

        return head.next



head = Node(0)

head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(0)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next = Node(0)

obj = Solution()
obj.display(head)
res = obj.optimized_zeros(head)
obj.display(res)
# print(res)