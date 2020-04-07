class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, x):
        if x < self.key:
            if self.left:
                self.left.insert(x)
            else:
                self.left = Node(x)
        elif x > self.key:
            if self.right:
                self.right.insert(x)
            else:
                self.right = Node(x)

    def upper_bound(self, x):
        if self.key <= x:
            if self.right:
                return self.right.upper_bound(x)
            return None
        if self.left == None:
            return self
        tmp = self.left.upper_bound(x)
        if tmp != None:
            return tmp
        return self

class Set:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root:
            self.root.insert(x)
        else:
            self.root = Node(x)

    def upper_bound(self, x):
        if self.root:
            return self.root.upper_bound(x)
        return None


n = int(input())
arr = list(map(int, input().split()))

s = Set()
newArr = []

for i in arr:
    if s.upper_bound(i) is not None:
        newArr.append(i - s.upper_bound(i).key)
    s.insert(i)
print(newArr)

print(min(newArr))
