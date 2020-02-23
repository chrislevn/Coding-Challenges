import sys
sys.setrecursionlimit(10005)


def DFS(scr):
    visited = [False] * (n + 1)
    s = [scr]
    visited[scr] = True
    nbombs = 0

    while len(s):
        u = s.pop()
        nbombs += 1

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)

    return nbombs


visited = [0] * 10005
path = [0] * 10005
graph = [[] for i in range(10005)]
count_arr = []
depth = 0

n, m = map(int, input().split())
result = 0

for j in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)

for j in range(n):

    DFS(j)
    if depth < DFS(j):
        depth = DFS(j)

print(depth)

