import queue
MAX = 30
INF = int(1e9)


def FloyWarshall(graph, dist, path):
    for i in range(MAX):
        for j in range(MAX):
            # print(graph[i][j])
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = graph[i][j]

            if graph[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1

    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]


n = int(input())

while n != 0:

    graph_young = [[INF for i in range(MAX)] for j in range(MAX)]
    graph_old = [[INF for i in range(MAX)] for j in range(MAX)]

    dist_young = [[INF for i in range(MAX)] for j in range(MAX)]
    dist_old = [[INF for i in range(MAX)] for j in range(MAX)]

    path_young = [[INF for i in range(MAX)] for j in range(MAX)]
    path_old = [[INF for i in range(MAX)] for j in range(MAX)]

    for i in range(n):
        arr = input().split()

        age = ord(arr[0]) - ord('A')
        type = ord(arr[1]) - ord('A')

        source = ord(arr[2]) - ord('A')
        end = ord(arr[3]) - ord('A')

        energy = int(arr[4])
        # print(age, type)

        # Young
        if age == 24:
            # B
            if type == 1:
                graph_young[source][end] = min(graph_young[source][end], energy)
                graph_young[end][source] = min(graph_young[end][source], energy)

            # U
            else:
                graph_young[source][end] = min(graph_young[source][end], energy)

        # Old
        if age == 12:
            # B
            if type == 1:
                graph_old[source][end] = min(graph_old[source][end], energy)
                graph_old[end][source] = min(graph_old[end][source], energy)

            # U
            else:
                graph_old[source][end] = min(graph_old[source][end], energy)

    FloyWarshall(graph_young, dist_young, path_young)
    FloyWarshall(graph_old, dist_old, path_old)

    arr_goal = input().split()
    s_young = ord(arr_goal[0]) - ord('A')
    s_old = ord(arr_goal[1]) - ord('A')

    sum_arr = []

    for f in range(26):
        res_y = dist_young[s_young][f]
        res_o = dist_old[s_old][f]

        # print(res_y, res_o)
        # print()
        sum_arr.append((res_y + res_o, f))

    result, index_value = min(sum_arr)

    if result >= INF:
        print("You will never meet.")
    else:
        print(result, chr(index_value + ord('A')))

    n = int(input())