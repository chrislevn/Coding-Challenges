MAX = 10000
parent = []
ranks = []


def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX * 2)]
    ranks = [0 for i in range(MAX * 2)]


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


n = int(input())
makeSet()

while True:
    c, x, y = map(int, input().split())
    if c == x == y == 0:
        break

    if c == 1:
        if findSet(x) == findSet(y + MAX):
            print(-1)
            continue
        unionSet(x, y)
        unionSet(x + MAX, y + MAX)
    elif c == 2:
        if findSet(x) == findSet(y):
            print(-1)
            continue
        unionSet(x, y + MAX)
        unionSet(x + MAX, y)
    elif c == 3:
        if findSet(x) == findSet(y):
            print(1)
        else:
            print(0)
    else:
        if findSet(x) == findSet(y + MAX):
            print(1)
        else:
            print(0)
