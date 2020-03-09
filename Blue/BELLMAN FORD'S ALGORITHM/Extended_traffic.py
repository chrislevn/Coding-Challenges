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
            w = graph[j].weight

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        # print(m)
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True


t = int(input())

for num_1 in range(t):
    blank = input()

    n = int(input())

    graph = []
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    arr_n = list(map(int, input().split()))

    m = int(input())
    for num_2 in range(m):
        source, destination = map(int, input().split())
        graph.append(Node(source, destination, (arr_n[destination - 1] - arr_n[source - 1])**3))

    q = int(input())
    s = 1
    print("Case " + str(num_1 + 1) + ":")

    BellmanFord(s)

    for num_2 in range(q):
        junction = int(input())

        if dist[junction] >= 3 and dist[junction] != INF:
            print(dist[junction])
        else:
            print("?")
