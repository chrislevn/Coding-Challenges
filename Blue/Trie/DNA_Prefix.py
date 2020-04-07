class Node:
    def __init__(self):
        self.common = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    level = 0
    global res
    resArr = []

    for ch in s:
        level += 1
        if ch in tmp.child:
            tmp = tmp.child[ch]
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
        tmp.common += 1
        resArr.append(level * tmp.common)
    ans = max(resArr)
    res = max(ans, res)

t = int(input())
for i in range(t):
    root = Node()

    n = int(input())
    res = 0 # level * temp
    temp = 0 #

    for j in range(n):
        letter = input()
        addWord(root, letter)

    print("Case " + str(i+1) + ": " + str(res))