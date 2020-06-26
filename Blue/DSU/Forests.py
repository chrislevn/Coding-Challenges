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
        return False
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1
    return True


if __name__ == "__main__":
    n = int(input())
    input()

    for i in range(n):
        graph = [[] for t in range(105)]
        makeSet()
        count = 0

        P, T = map(int, input().split())
        numbers = list(map(int, input().split()))
        while len(numbers) > 0:
            y = numbers[0]
            j = numbers[1]
            graph[y].append(j)

            try:
                numbers = list(map(int, input().split()))
            except EOFError:
                break

        for q in range(1, P+1):
            graph[q].sort()

        res = P
        for q in range(1, P+1):
            for e in range(q, P+1):
                if graph[q] == graph[e]:
                    if unionSet(q, e):
                        res -= 1

        print(res)
        if i < n-1:
            print()
