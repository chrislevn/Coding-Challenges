MAX = 100
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
makeSet()

if n != m or n < 3:
    print("NO")
    exit()

for i in range(m):
    x, y = map(int, input().split())
    unionSet(x, y)

ans = findSet(1)
for i in range(1, n+1):
    if ans != findSet(i):
        print("NO")
        exit()
print("FHTAGN!")