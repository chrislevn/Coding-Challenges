import sys
sys.setrecursionlimit(10005)

def DFS(src):
    global count_loop
    u = src
    visited[src] = 1

    for v in graph[u]:
        if visited[v] == 0:
            visited[v] = 1
            path[v] = u
            DFS(v)

        elif visited[v] == 1:
            count_loop += 1
            
    visited[u] = 2

T = int(input())
for i in range(T):
    visited = [0] * 100000
    path = [0] * 100000
    graph = [[] for i in range(100000)]
    count_loop = 0

    n, m = map(int, input().split())

    for j in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        graph[a].append(b)
       
    for j in range(n):
        if visited[j] == False:
            DFS(j)

    # print(count_loop)

    if count_loop == 0:
        print("NO")
    else:
        print("YES")