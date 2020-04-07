class Node:
    def __init__(self):
        self.common = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    global res
    resArr = []

    for ch in s:
        if ch in tmp.child:
            tmp = tmp.child[ch]
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
        tmp.common += 1
        resArr.append(tmp.common)
    ans = max(resArr)
    res = max(ans, res)


def findWord(root, s):
     tmp = root
     global count
     for ch in s:
         if ch not in tmp.child:
            return False
         tmp = tmp.child[ch]
     count = tmp.common
     return tmp.common > 0


n = int(input())
root = Node()
for i in range(n):
    letter = list(map(str, input().split()))
    command = letter[0]
    word = letter[1]
    res = 0
    count = 0

    if command == "add":
        addWord(root, word)

    if command == "find":
        if findWord(root, word):
            print(count)
        else:
            print(0)
