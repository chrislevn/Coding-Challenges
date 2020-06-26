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

    def calculate_height(self):
        height_left = 0
        height_right = 0
        if self.left:
            height_left = self.left.calculate_height()
        if self.right:
            height_right = self.right.calculate_height()

        return max(height_left, height_right) + 1


class BST:
    def __init__(self):
        self.root = None

    def add(self, data=0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def calculate_height(self):
        return self.root.calculate_height()


value = BST()
for i in arr:
    value.add(i)

print(value.calculate_height())


def pathToNode(root, path, k):
    if root is None:
        return False

    path.append(root.data)
    if root.data == k:
        return True

    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)

        path2 = []
        pathToNode(root, path2, data2)
        i = 0
        while i < len(path1) and i < len(path2):

            if path1[i] != path2[i]:
                break
            i = i + 1

        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0