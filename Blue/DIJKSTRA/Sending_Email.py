import queue

MAX = 10000
INF = int(1e9)


class Node:
    def __init__(self, id, dist) :
        self.dist = dist
        self.id = id

    def __lt__(self, other) :
        return self.dist <= other.dist


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u




q = int(input())

for i in range(q):
    graph = [[] for _ in range(MAX + 5)]
    dist = [INF for _ in range(MAX + 5)]
    path = [-1 for _ in range(MAX + 5)]

    n, m, s, t = map(int, input().split())

    for j in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    Dijkstra(s)
    result = dist[t]

    if result == INF:
        print("Case #" + str(i + 1) + ": unreachable")
    else:
        print("Case #" + str(i + 1) + ": " + str(result))
