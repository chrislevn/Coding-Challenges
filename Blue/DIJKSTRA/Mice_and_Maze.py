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


n = int(input())
e = int(input())
t = int(input())

m = int(input())

countMice = 0

for i in range(m):
    a, b, time = map(int, input().split())
    graph[a].append(Node(b, time))
    # graph[b].append(Node(a, time))


for i in range(1, n + 1):
    dist = [INF for _ in range(MAX + 5)]
    path = [-1 for _ in range(MAX + 5)]

    Dijkstra(i)
    timeTravel = dist[e]
    # print("Time", timeTravel)

    if timeTravel <= t:
        # print(i)
        countMice += 1

print(countMice)


