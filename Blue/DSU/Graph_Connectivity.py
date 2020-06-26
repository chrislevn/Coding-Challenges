import sys

MAX = 26
parent = []
ranks = []

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])

    return parent[u]


def unionSet(u, v):

    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1
    return True


n = int(input())
input()

for i in range(n):
    makeSet()
    count = 0

    check = input()
    res = ord(check) - 64

    letter = list(input())

    while len(letter) > 0:
        letter = list(letter)
        u = ord(letter[0]) - 65
        v = ord(letter[1]) - 65
        if unionSet(u, v):
            res -= 1

        try:
            letter = list(input())
        except EOFError:
            break
    print(res)
    if i <= n-2:
        print()
