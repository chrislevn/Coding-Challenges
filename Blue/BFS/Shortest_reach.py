from queue import Queue

MAX = 1000

visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]


def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1

    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u


def calculatePath(s, f):
    b = []

    if path[f] == -1:
        return -1

    while True:
        b.append(f)
        f = path[f]

        if f == s:
            break

    return len(b)*6

Q = int(input())

for j in range(Q):
    visited = [False for i in range(MAX)]
    path = [0 for i in range(MAX)]
    graph = [[] for i in range(MAX)]

    n, m = map(int, input().split())
    V, E = n, m
    for l in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    s = int(input())
    s -= 1
    BFS(s)
    for f in range(0, n):
        if f != s:
            print(calculatePath(s, f), end=' ')
    print()



