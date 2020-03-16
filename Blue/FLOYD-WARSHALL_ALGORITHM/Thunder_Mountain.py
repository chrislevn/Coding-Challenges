import math
MAX = 100
INF = int(1e9)


def FloyWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def calculateDist(x1, y1, x2, y2):
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)


testCase = int(input())
for i in range(testCase):
    n = int(input())

    graph = [[INF if i != j else 0 for j in range(n)] for i in range(n)]
    map_graph = []
    dist = [[INF for i in range(n)] for j in range(n)]

    for j in range(n):
        x, y = map(int, input().split())
        map_graph.append((x, y))

    for j in range(n):
        for k in range(n):
            x1 = map_graph[j][0]
            y1 = map_graph[j][1]

            x2 = map_graph[k][0]
            y2 = map_graph[k][1]

            distance = calculateDist(x1, y1, x2, y2)
            if distance > 10:
                continue

            graph[j][k] = distance
            graph[k][j] = distance

    FloyWarshall(graph, dist)

    res = dist[0][0]
    for j in range(n):
        for k in range(n):
            if dist[j][k] > res:
                res = dist[j][k]

    print("Case #" + str(i + 1) + ":")

    if res >= INF:
        print("Send Kurdy")
    else:
        print(format(res, '.4f'))
    print()