import queue

MAX = 10000
INF = int(1e9)


class Node:
    def __init__(self, id, dist) :
        self.dist = dist
        self.id = id

    def __lt__(self, other) :
        return self.dist <= other.dist


def Dijkstra(s, graph, dist):
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




t = int(input())

for i in range(t):
    graph = [[] for _ in range(MAX + 5)]

    dist = [INF for _ in range(MAX + 5)]
    otherDist = [INF for _ in range(MAX + 5)]

    path = [-1 for _ in range(MAX + 5)]


    n = int(input())
    r = int(input())

    for j in range(r):
        u, v = map(int, input().split())
        graph[u].append(Node(v, 1))
        graph[v].append(Node(u, 1))

    s, d = map(int, input().split())

    result_arr = []
    Dijkstra(s, graph, otherDist)
    Dijkstra(d, graph, dist)

    for j in range(n):
        result_arr.append(dist[j] + otherDist[j])

    result = max(result_arr)
    print("Case " + str(i + 1) + ": " + str(result))