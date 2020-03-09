import queue
MAX = 100
INF = int(1e9)


def printPath(s, f):
    b = []
    while s != f:
        b.append(f)
        f = path[s][f]
    b.append(s)

    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=' ' if i > 0 else '\n')


def FloyWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            # print(graph[i][j])
            if graph[i][j] == 'Y':
                # print("Okay")
                dist[i][j] = 1
            else:
                dist[i][j] = INF

            if i == j:
                dist[i][j] = 0

            if graph[i][j] != INF and i != j:
                path[i][j] = 1
            else:
                path[i][j] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]


t = int(input())

for num_1 in range(t):
    process_arr = []

    arr = input()
    process_arr.append(arr)
    n = len(arr)

    for num_2 in range(n - 1):
        arr = input()
        process_arr.append(arr)

    graph = [[None for i in range(n)] for j in range(n)]
    dist = [[None for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            graph[i][j] = process_arr[i][j]

    FloyWarshall(graph, dist)
    # print(dist)

    num_friends, index = 0, 0

    for i in range(n):
        count = 0

        for j in range(n):
            if dist[i][j] == 2:
                count += 1

        if count > num_friends:
            num_friends = count
            index = i

    print(index, num_friends)
