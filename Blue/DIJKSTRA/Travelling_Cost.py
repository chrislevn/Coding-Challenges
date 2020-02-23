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


graph = [[] for _ in range(MAX + 5)]
dist = [INF for _ in range(MAX + 5)]
path = [-1 for _ in range(MAX + 5)]

n = int(input())
for i in range(n):
    a, b, w = map(int, input().split())
    graph[a].append(Node(b, w))
    graph[b].append(Node(a, w))

u = int(input())
q = int(input())

for i in range(q):
    v = int(input())
    Dijkstra(u)
    cost = dist[v]

    if cost >= INF:
        cost = "NO PATH"
    print(cost)

# s, t = 0, 4

#
# for i in range(n):
#     d = list(map(int, input().split()))
#     for j in range(n):
#         if d[j] > 0:
#             graph[i].append(Node(j, d[j]))
#             Dijkstra(s)
#             ans = dist[t]
#             print(ans)

# n = int(input())
#
# for i in range(n):
#