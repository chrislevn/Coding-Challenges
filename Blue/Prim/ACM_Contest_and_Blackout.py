import queue

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
     ans = 0
     for i in range(1, n+1):
        if path[i] == -1:
            continue
        ans += dist[i]
     return ans


def getPoint():
    for i in range(1, n+1):
        if path[i] == -1:
            continue
        point.append((path[i], i))


def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in range(1, n+1):
            v = neighbor
            w = graph[u][v]

            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


t = int(input())
for i in range(t):
    n, m = map(int, input().split())

    graph = [[INF for x in range(n+1)] for i in range(n+1)]
    dist = [INF for i in range(n + 1)]
    path = [-1 for i in range(n + 1)]
    visited = [False for i in range(n + 1)]

    point = []
    res_2 = []

    for j in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    Prim(1)

    res = printMST()
    getPoint()
    # print(point)

    for j in range(len(point)):
        dist = [INF for i in range(n + 1)]
        path = [-1 for i in range(n + 1)]
        visited = [False for i in range(n + 1)]

        u, v = point[j][0], point[j][1]
        tmp = graph[u][v]
        graph[u][v] = INF
        graph[v][u] = INF

        Prim(1)
        flag = True

        for l in range(1,n+1):
            if dist[l] == INF:
                flag = False
                break
        if flag:
            res_2.append(printMST())

        graph[u][v] = tmp
        graph[v][u] = tmp

    print(res, min(res_2))

