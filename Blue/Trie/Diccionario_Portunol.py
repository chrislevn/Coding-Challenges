import string
import sys
sys.setrecursionlimit(10000000)


class Node:
    def __init__(self):
        self.countLeaf = 0
        self.child = dict()


def suffix_traversal(root, level, startWith):
    cnt = 1
    for c in root.child:
        if level > 0:
            startWith[c] += 1
        cnt += suffix_traversal(root.child[c], level + 1, startWith)
    return cnt


def prefix_traversal(root, level, suffix_state_count, startWith):
    res = 0
    if level > 0:
        res = suffix_state_count
    for c in root.child:
        if level > 0:
            res -= startWith[c]
        res += prefix_traversal(root.child[c], level + 1, suffix_state_count, startWith)

    return res


def addWord(root, s):
    tmp = root
    for ch in s:
        if ch in tmp.child:
            tmp = tmp.child[ch]
        else:
            tmp.child[ch] = Node()
            tmp = tmp.child[ch]
    tmp.countLeaf += 1


p, s = map(int, input().split())

while p != 0 and s != 0:
    strList = dict()

    rootPot = Node()
    for i in range(p):
        potLetter = input()
        addWord(rootPot, potLetter)

    rootSpan = Node()
    for i in range(s):
        letter = input()
        letterArr = list(letter)
        letterArr.reverse()
        spanLetter = "".join(letterArr)

        addWord(rootSpan, spanLetter)
    startWith = {c: 0 for c in string.ascii_lowercase}
    suffix_state_count = suffix_traversal(rootPot, 0, startWith) - 1
    print(prefix_traversal(rootSpan, 0, suffix_state_count, startWith))

    p, s = map(int, input().split())


