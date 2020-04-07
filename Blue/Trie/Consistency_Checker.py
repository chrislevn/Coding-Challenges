class Node:
    def __init__(self):
        self.countLeaf = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    global flag
    for i in range(len(s)):
        ch = s[i]
        if ch in tmp.child:
            tmp = tmp.child[ch]
            if tmp.countLeaf > 0 or i == len(s) - 1:
                flag = False
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
    tmp.countLeaf += 1


t = int(input())
for i in range(t):
    n = int(input())
    root = Node()
    flag = True
    for j in range(n):
        strNum = input()
        addWord(root, strNum)
    if flag:
        print("Case " + str(i+1) + ": YES")
    else:
        print("Case " + str(i+1) + ": NO")
