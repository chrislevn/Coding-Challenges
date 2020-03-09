from queue import Queue

MAX = 110
INF = int(1e9)


class Node:
    def __init__(self, source, target):
        self.source = source
        self.target = target


def hasPath(s, f):
    distance = [-1] * MAX
    q = Queue()
    q.put(s)
    distance[s] = 0

    while not q.empty():
        u = q.get()

        for i in graph:
            if i.source == u:
                v = i.target

                if distance[v] == -1:
                    q.put(v)
                    distance[v] = 0

                if v == f:
                    return True
    return False


def BellmanFord(s, f):
    global dist
    global graph
    global path

    dist[s] = 100
    for i in range(n -1):
        for edge in graph:
            # print(m)

            u = edge.source
            v = edge.target
            w = weight[v]

            if dist[u] > 0 and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    for edge in graph:
        # print(m)
        u = edge.source
        v = edge.target
        w = weight[v]

        if dist[u] > 0 and dist[u] + w > dist[v] and hasPath(u,f):
            return True


    if dist[f] > 0:
        return True
    else:
        return False


n = int(input())


while (n != -1):

    graph = []
    dist = [-INF for num in range(n + 5)]
    path = [-1 for num in range(n + 5)]
    weight = [-1 for num in range(n + 5)]

    for i in range(n):
        arr = list(map(int, input().split()))

        weight_source = arr[0]
        weight[i+1] = weight_source

        source = i+1
        dest_arr = arr[2:]

        for dest in dest_arr:
            graph.append(Node(source, dest))

    s = 1
    res = BellmanFord(s, n)
    # print(dist)

    if not res:
        print("hopeless")
    else:
        print("winnable")

    n = int(input())


