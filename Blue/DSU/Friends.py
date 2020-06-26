def makeSet():
    global parent, ranks, count
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]
    count = [1 for i in range(MAX + 5)]


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
        count[up] += count[vp]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        count[vp] += count[up]
    else:
        parent[up] = vp
        ranks[vp] += 1
        count[vp] += count[up]


t = int(input())

for i in range(t):
    MAX = 30000
    parent = []
    ranks = []
    count = []

    n, m = map(int, input().split())
    makeSet()

    for j in range(m):
        a, b = map(int, input().split())
        unionSet(a, b)

    print(max(count))