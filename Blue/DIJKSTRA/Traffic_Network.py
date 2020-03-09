import queue

MAX = 100000
INF = int(1e9)


class Node:
    def __init__(self, id, dist) :
        self.dist = dist
        self.id = id

    def __lt__(self, other) :
        return self.dist <= other.dist


# def Dijkstra(s, dist, graph):
#     pq = [(0, s)]
#     dist[s] = 0
#
#     while pq:
#         w, u = heappop(pq)
#
#         if w > dist[u]:
#             continue
#
#         for weight, v in graph[u]:
#             if w + weight < dist[v]:
#                 dist[v] = w + weight
#                 heappush(pq, (dist[v], v))

def Dijkstra_1(s, otherDist, otherGraph):
    pq = queue.PriorityQueue()

    pq.put(Node(s, 0))
    otherDist[s] = 0

    while (pq.empty() == False):
        top = pq.get()

        u = top.id
        w = top.dist

        for neighbor in otherGraph[u]:
            if w + neighbor.dist < otherDist[neighbor.id]:
                otherDist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, otherDist[neighbor.id]))
                path_1[neighbor.id] = u

# def Dijkstra_2(s):
#     pq = queue.PriorityQueue()
#     pq.put(Node(s, 0))
#     dist_2[s] = 0
#     while pq.empty() == False:
#         top = pq.get()
#         u = top.id
#         w = top.dist
#         for neighbor in graph_2[u]:
#             if w + neighbor.dist < dist_2[neighbor.id]:
#                 dist_2[neighbor.id] = w + neighbor.dist
#                 pq.put(Node(neighbor.id, dist_2[neighbor.id]))
#                 # path_2[neighbor.id] = u



dataNum = int(input())

for i in range(dataNum):
    graph_1 = [[] for _ in range(MAX + 5)]
    graph_2 = [[] for _ in range(MAX + 5)]

    dist_1 = [INF for _ in range(MAX + 5)]
    dist_2 = [INF for _ in range(MAX + 5)]

    path_1 = [-1 for _ in range(MAX + 5)]
    path_2 = [-1 for _ in range(MAX + 5)]

    n, m, k, s, t = map(int, input().split())
    for x in range(m):
        d, c, l = map(int, input().split())
        graph_1[d].append(Node(c, l))
        graph_2[c].append(Node(d, l))

    # for x in range(k):
    #     u, v, q = map(int, input().split())
    #     graph_2[u].append(Node(v, q))
    #     graph_2[v].append(Node(u, q))

    Dijkstra_1(s, dist_1,graph_1)
    Dijkstra_1(t, dist_2, graph_2)
    cost = dist_1[t]

    result = cost

    for x in range(k):
        u, v, q = map(int, input().split())
        if dist_1[u] + q + dist_2[v] < result:
            result = dist_1[u] + q + dist_2[v]
        if dist_1[v] + q + dist_2[u] < result:
            result = dist_1[v] + q + dist_2[u]

    if (result == INF) or (result == INF):
        print(-1)
    else:
        print(result)
