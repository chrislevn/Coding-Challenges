from queue import Queue

MAX = 100000 + 5
visited = [False for i in range(MAX)]
graph = [[] for _ in range(MAX)]

cat = [0] * MAX

def BFS(s):
    num_res = 0

    q = Queue()
    visited[s] = True
    q.put(s)

    if arr[s] == 1:
        cat[s] = 1
    else:
        cat[s] = 0

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True

                if arr[v] == 1:
                    cat[v] = cat[u] + 1

                if cat[v] <= m:
                    if len(graph[v]) == 1:
                        num_res += 1

                    else:
                        q.put(v)
    return num_res


n, m = map(int, input().split())
arr = [None] + list(map(int, input().split()))

for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(BFS(1))

