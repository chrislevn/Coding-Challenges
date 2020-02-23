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

    def is_double(self):
        return self.left and self.right

    def count_double(self):
        count = 0
        if self.is_double():
            count = 1
        if self.right:
            count += self.right.count_double()
        if self.left:
            count += self.left.count_double()

        return count


class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def count_double(self):
        return self.root.count_double()


value = BST()

for i in arr:
    value.add(i)

print(value.count_double())