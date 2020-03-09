MAX = 100
INF = int(1e9)


# class Node:
#     def __init__(self, source, target, weight):
#         self.source = source
#         self.target = target
#         self.weight = weight


def BellmanFord(s):
    global dist
    global graph
    global path

    dist[s] = 0

    for i in range(1, n):
        for j in range(m):
            # print(m)
            u, v, w = graph[j]

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF


n, m, q, s = map(int, input().split())

while not (n == 0 and m == 0 and q == 0 and s == 0):

    graph = []
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for num_1 in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    BellmanFord(s)
    # print(dist)

    for num_1 in range(q):
        f = int(input())

        if dist[f] == -INF:
            print("-Infinity")
        elif dist[f] == INF:
            print("Impossible")
        else:
            print(dist[f])

    print()

    n, m, q, s = map(int, input().split())

