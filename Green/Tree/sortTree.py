import sys
sys.setrecursionlimit(10000)

n = int(input())
arr = list(map(int, input().split()))

class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def add(self, x):
        if x < self.data:
            if self.left:
                self.left.add(x)
            else:
                self.left = Node(x)
        elif self.data < x:
            if self.right:
                self.right.add(x)
            else:
                self.right = Node(x)

    def output_order(self):
        if self.left:
            self.left.output_order()
        print(self.data, end = ' ')
        if self.right:
            self.right.output_order()


class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def output_order(self):
        self.root.output_order()

value = BST()
for i in arr:
    value.add(i)

value.output_order()