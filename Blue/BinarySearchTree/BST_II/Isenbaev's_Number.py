from queue import Queue

MAX = 1000
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]


def BFS(graph, s, rank, n):
    rank[s] = 0
    for i in range(n):
        visited[i] = False
        path[i] = -1

    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
                rank[v] = rank[u] + 1
    return rank


n = int(input())
s = dict()
count = 0
graph = []
for i in range(n):
    letter = list(input().split(" "))
    arr = []
    for j in letter:
        if j in s:
            id = s[j]
        else:
            s[j] = count
            id = count
            graph.append([])
            count += 1
        arr.append(id)
    for x in arr:
        for y in arr:
            if x != y:
                graph[x].append(y)

rank = ['undefined' for i in range(count)]
if 'Isenbaev' in s:
    rank = BFS(graph, s['Isenbaev'], rank, len(s))
a = []
for name in s:
    a.append(name)
a.sort()
for name in a:
    print(name + ' ' + str(rank[s[name]]))




