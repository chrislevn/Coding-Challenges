MAX = 100
INF = int(1e9)


def FloyWarshall(graph, dist):
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            dist[i][j] = graph[i][j]

    for _ in range(2):
        for k in range(1, c + 1):
            for i in range(1, c + 1):
                for j in range(1, c + 1):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast


c, r, q = map(int, input().split())
count = 1

while c != 0 and r != 0 and q != 0:
    graph = [[INF if i != j else 0 for j in range(c + 5)] for i in range(c + 5)]
    dist = [[INF for i in range(c + 5)] for j in range(c + 5)]
    maxCost = [[INF for i in range(c + 5)] for j in range(c + 5)]

    f = [0] + list(map(int, input().split()))
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            maxCost[i][j] = max(f[i], f[j])

    for num_1 in range(r):
        c1, c2, d = map(int, input().split())
        graph[c1][c2] = d
        graph[c2][c1] = d

    if count > 1:
        print()

    print("Case #" + str(count))
    FloyWarshall(graph, dist)

    for num_1 in range(q):
        start, end = map(int, input().split())
        res = dist[start][end] + maxCost[start][end]

        if res > INF:
            print(-1)
        else:
            print(res)
    count += 1
    c, r, q = map(int, input().split())

