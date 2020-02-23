# 5 1 2 7 6 8
#       5
#     1         7
#       2   6       8

import sys
sys.setrecursionlimit(10000)


n = int(input())
arr = list(map(int, input().split()))


class Node:
    def __init__(self, x=0, left=None, right=None):
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

    def even_output(self):
        if self.left:
            self.left.even_output()
        if self.right:
            self.right.even_output()
        if self.data % 2 == 0 and self.data is not None:
            print(self.data, end=" ")


class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def even_output(self):
        self.root.even_output()

value = BST()

for i in arr:
    value.add(i)

value.even_output()

