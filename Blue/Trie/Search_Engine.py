class Node:
    def __init__(self):
        self.child = dict()
        self.maxValue = -1

def addWord(root, s, value):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        tmp = tmp.child[c]
        tmp.maxValue = max(tmp.maxValue, value)

def getHeighestMatching(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            return -1
        tmp = tmp.child[c]
    return tmp.maxValue

n, q = map(int, input().strip().split())
root = Node()

for i in range(n):
    line = input().strip().split()
    addWord(root, line[0], int(line[1]))

for i in range(q):
    s = input().strip()
    print(getHeighestMatching(root, s))