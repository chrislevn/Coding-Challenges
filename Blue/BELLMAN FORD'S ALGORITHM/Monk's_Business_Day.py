MAX = 100
INF = int(1e9)


class Node:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def BellmanFord(s):
    global dist
    global graph
    global path

    dist[s] = 0

    for i in range(1, n):
        for j in range(m):
            # print(m)
            u = graph[j].source
            v = graph[j].target
            w = -graph[j].weight

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        # print(m)
        u = graph[i].source
        v = graph[i].target
        w = -graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return True
    return False


t = int(input())

for num_1 in range(t):
    n, m = map(int, input().split())

    graph = []
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for num_2 in range(m):
        i, j, C = map(int, input().split())
        graph.append(Node(i, j, C))

    s = 1
    BellmanFord(s)

    res = BellmanFord(s)

    if res:
        print("Yes")
    else:
        print("No")