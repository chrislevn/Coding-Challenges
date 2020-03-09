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

    dist[s] = 100

    for i in range(1, n):
        for j in range(m * 2):
            # print(m)
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight / 100

            if dist[u] != -INF and dist[u] * w > dist[v]:
                dist[v] = dist[u] * w
                path[v] = u
    for i in range(m * 2):
        # print(m)
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight / 100
        if dist[u] != -INF and dist[u] * w > dist[v]:
            return False
    return True


arr = list(map(int, input().split()))


while len(arr) > 1:
    n = arr[0]
    m = arr[1]

    graph = []
    dist = [-INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for num in range(m):
        a, b, p = map(int, input().split())
        graph.append(Node(a, b, p))
        graph.append(Node(b, a, p))

    q = n
    s = 1
    res = BellmanFord(s)
    print("{:.6f} percent".format(dist[q]))

    arr = list(map(int, input().split()))

