MAX = 50000 + 5
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


n, m = map(int, input().split())
case = 1

while n != 0 and m != 0:
    makeSet()

    for _ in range(m):
        i, j = map(int, input().split())
        unionSet(i, j)

    arr = []
    s = set()
    for b in range(1, n+1):
        s.add(findSet(b))

    print("Case " + str(case) + ": " + str(len(s)))

    case += 1
    n, m = map(int, input().split())
