import sys
sys.setrecursionlimit(10000)

n, number = map(int, input().split())
arr = list(map(int, input().split()))

# 5 1 2 7 6 8
# 5 1 2 = 8
#       5
#     1         7
#       2   6       8

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

    def sum_smaller(self, x):
        sum = 0
        if self.data < x:
            sum += self.data
        if self.left:
            sum += self.left.sum_smaller(x)

        if self.right:
            sum += self.right.sum_smaller(x)

        return sum



class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def sum_smaller(self, y):
        return self.root.sum_smaller(y)


value = BST()

for i in arr:
    value.add(i)

print(value.sum_smaller(number))
