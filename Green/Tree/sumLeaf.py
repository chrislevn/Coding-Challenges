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

    def leaf(self):
        return self.left is None and self.right is None

    def sum_leaf(self):
        sum = 0
        if self.left:
            sum += self.left.sum_leaf()
        if self.right:
            sum += self.right.sum_leaf()
        if self.leaf():
            return self.data
        return sum


class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def sum_leaf(self):
        return self.root.sum_leaf()


value = BST()
for i in arr:
    value.add(i)

print(value.sum_leaf())
