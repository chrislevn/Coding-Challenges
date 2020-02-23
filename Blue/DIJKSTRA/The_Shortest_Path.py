import queue

MAX = 1000000
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


s = int(input())

for x in range(s):
    n = int(input())

    graph = [[] for _ in range(n + 5)]
    saveName = []

    for i in range(1, n + 1):
        cityName = str(input()).lower()
        p = int(input())

        saveName.append(cityName)

        for j in range(p):
            nr, cost = map(int, input().split())
            graph[i].append(Node(nr, cost))

    r = int(input())

    for i in range(r):
        source, destination = map(str, input().split())
        source, destination = source.lower(), destination.lower()

        dist = [INF for _ in range(n + 5)]
        path = [-1 for _ in range(n + 5)]

        sourceIndex = saveName.index(source) + 1
        desIndex = saveName.index(destination) + 1

        # print(sourceIndex, desIndex)

        Dijkstra(sourceIndex)
        costValue = dist[desIndex]

        print(costValue)

    empty = input()


