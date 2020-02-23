visited = [False] * 100000
path = [0] * 100000
graph = [[] for i in range(100000)]

result = []

def DFS(src):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s[-1]
        #$if u in hasGirl:
        s.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                s.append(v)
                path[v] = u

def printPath(s, f, path):
    b = []
    if f == s:
        #print(f)
        return
    if path[f] == -1:
        print("No path")
        return
    while True:
        b.append(f)
        f = path[f]

        if f == s:
            b.append(s)
            break


    result.append((len(b) - 1, b[0]))


if __name__ == '__main__':
    hasGirl = []
    noGirl = []

    N = int(input())
    V = N
    E = N-1
    for i in range(N-1):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        graph[u].append(v)
        graph[v].append(u)

    q = int(input())
    s = 0
    DFS(s)

    for i in range(q):
        k = int(input())
        hasGirl.append(k)

        f = hasGirl[i] - 1
        printPath(s, f, path)

    result.sort()
    order, index = result[0]

    print(index + 1)