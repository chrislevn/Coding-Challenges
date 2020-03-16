MAX = 100
INF = int(1e9)
n = 25


def FloyWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


count = 1

while True:
    try:
        graph = [[INF if i != j else 0 for j in range(n)] for i in range(n)]
        dist = [[INF for i in range(n)] for j in range(n)]

        for num_1 in range(1, 20):
            arr = list(map(int, input().split()))
            i = num_1

            for num_2 in arr[1:]:
                graph[i][num_2] = 1
                graph[num_2][i] = 1

        nT = int(input())

        # print(graph)
        FloyWarshall(graph, dist)
        # print(dist)

        print("Test Set #" + str(count))
        for num_1 in range(nT):
            start, end = map(int, input().split())
            print('{:2d} to {:2d}: {}'.format(start, end, dist[start][end]))

        count += 1
        print()

    except EOFError:
        break