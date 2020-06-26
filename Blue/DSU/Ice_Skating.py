MAX = 1000
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
    global count
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    count -= 1

    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


n = int(input())
coord = []
count = n
makeSet()

for i in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

for i in range(len(coord)):
    for j in range(len(coord)):
        if coord[i][0] == coord[j][0] or coord[i][1] == coord[j][1]:
            unionSet(coord[i][0], coord[i][1])

print(count)
