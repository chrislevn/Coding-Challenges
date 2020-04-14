import queue
import math

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
     ans = 0
     for i in range(n):
        if path[i] == -1:
            continue
        ans += dist[i]
     return ans

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in range(n):
            if visited[neighbor] == False and graph[u][neighbor] < dist[neighbor]:
                dist[neighbor] = graph[u][neighbor]
                pq.put(Node(neighbor, graph[u][neighbor]))
                path[neighbor] = u


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

while True:
    try:
        n = int(input())

        dist = [INF for i in range(n + 1)]
        path = [-1 for i in range(n + 1)]
        visited = [False for i in range(n + 1)]

        point = []

        for i in range(n):
            x, y = map(int, input().split())
            point.append((x, y))

        graph = []
        for j in range(n):
            graph.append([])
            for k in range(n):

                graph[j].append(distance(point[j][0], point[j][1], point[k][0], point[k][1]))

        m = int(input())
        for i in range(m):
            a, b = map(int, input().split())
            graph[a - 1][b - 1] = 0
            graph[b - 1][a - 1] = 0

        Prim(0)
        res = printMST()
        print("%.2f" % res)

    except EOFError:
        exit()






