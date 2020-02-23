def DFS(src):
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s[-1]
        s.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                s.append(v)
                path[v] = u


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        visited = [False] * 100000
        path = [0] * 100000
        graph = [[] for i in range(100000)]
        count_brige = 0

        N = int(input())
        E = int(input())

        for j in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        for j in range(N):
            if visited[j] == False:
                DFS(j)
                count_brige += 1
        print(count_brige)