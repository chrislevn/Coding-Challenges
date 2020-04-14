class Node:
    def __init__(self):
        self.countLeaf = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    global flag
    global res
    for i in range(len(s)):
        ch = s[i]
        if ch in tmp.child:
            tmp = tmp.child[ch]
            if tmp.countLeaf > 0 or i == len(s) - 1:
                res = s
                flag = False
                break
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
    tmp.countLeaf += 1


n = int(input())
flag = True
res = ""
root = Node()
for i in range(n):
    letter = input()
    if flag:
        addWord(root, letter)

if flag:
    print("GOOD SET")
else:
    print("BAD SET")
    print(res)


