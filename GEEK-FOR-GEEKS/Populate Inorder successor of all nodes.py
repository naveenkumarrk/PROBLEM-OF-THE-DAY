class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:

    def insert(self, key):
        new_node = Node(key)
        if root.

    def populateNext(self, root):
        if root:
            self.populateNext(root.left)
            print(root.data)
            self.populateNext(root.right)

        
        