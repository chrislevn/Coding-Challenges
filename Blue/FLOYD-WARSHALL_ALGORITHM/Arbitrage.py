import queue
MAX = 100
INF = int(1e9)


def FloyWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]


n = int(input())
count_case = 1

while (n != 0):
    cost = 0
    currencyLetter = []

    graph = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    dist = [[None for i in range(n)] for j in range(n)]

    for num_1 in range(n):
        input_letter = input()
        currencyLetter.append(input_letter)

    m = int(input())
    for i in range(m):
        arr = list(input().split(" "))

        source = currencyLetter.index(arr[0])
        end = currencyLetter.index(arr[2])

        cost = arr[1]
        graph[source][end] = float(cost)

    FloyWarshall(graph, dist)
    temp = -INF

    for i in currencyLetter:
        res = dist[currencyLetter.index(i)][currencyLetter.index(i)]

        if temp < res:
            temp = res

    # print(temp)
    # print(dist)

    if temp > 1:
        print("Case " + str(count_case) + ": Yes")
    else:
        print("Case " + str(count_case) + ": No")

    blank = input()

    n = int(input())
    count_case += 1