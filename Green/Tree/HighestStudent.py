import sys
sys.setrecursionlimit(10000)


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score


class Node:
    def __init__(self, x = 0, left = None, right= None):
        self.data = x
        self.left = left
        self.right = right

    def add(self, x):
        if x.score < self.data.score:
            if self.left:
                self.left.add(x)
            else:
                self.left = Node(x)

        elif self.data.score < x.score:
            if self.right:
                self.right.add(x)
            else:
                self.right = Node(x)

    def best_student(self):
        if self.right:
            return self.right.best_student()
        return self.data



class BST:
    def __init__(self):
        self.root = None

    def add(self, data = 0):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def best_student(self):
        return self.root.best_student()


value = BST()

n = int(input())
for i in range(n):
    id, name, score = input().split(' ')
    score = float(score)
    value.add(Student(id, name, score))

result = value.best_student()

print(result.id, result.name, result.score)


