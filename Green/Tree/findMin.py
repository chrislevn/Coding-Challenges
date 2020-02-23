import sys
sys.setrecursionlimit(10000)

n = int(input())
arr = list(map(int, input().split()))

class Node:
    def __init__(self, x = 0, left = None, right= None):
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

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data


class BST:
    def __init__(self):
        self.root = None

    def add(self, data = 0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def min(self):
        return self.root.min()


value = BST()
for i in arr:
    value.add(i)

print(value.min())