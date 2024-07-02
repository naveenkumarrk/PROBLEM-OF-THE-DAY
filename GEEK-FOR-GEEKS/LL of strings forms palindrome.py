
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def compute(head): 
    #return True/False
    string = ""
    while head:
        string += head.data
        head = head.next
        
    return string == string[::-1]
        

head = Node('a')
head.next = Node('bc')
head.next.next = Node('d')
head.next.next.next = Node('dcb')
head.next.next.next.next = Node('a')

res= compute(head)
print(res)