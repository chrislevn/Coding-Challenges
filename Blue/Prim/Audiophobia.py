import queue

INF = 1e9


def DFS(src):
    for i in range(1,c+1):
        visited_res[i] = False
        path_res[i] = (-1, -1)
    s = []
    visited_res[src] = True
    s.append(src)
    while len(s) > 0:
        u = s[-1]
        s.pop()
        for neighbor in graph_res[u]:
            w = neighbor.dist
            v = neighbor.id
            if not visited_res[v]:
                visited_res[v] = True
                s.append(v)
                path_res[v] = (u,w)



def printPath(s, f, path_res):
    b = []
    res = []
    if f == s:
        #print(f)
        return
    if path_res[f] == (-1, -1):
        print("no path")
        return
    while True:
        b.append(path_res[f][1])
        f = path_res[f][0]

        if f == s:
            break

    print(max(b))


'''

'''

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
     ans = 0
     for i in range(1,c+1):
        if path[i] == -1:
            continue
        ans += dist[i]
        # print("{0} - {1}: {2}".format(path[i], i, dist[i]))
        u = path[i]
        v = i
        graph_res[u].append(Node(v, dist[i]))
        graph_res[v].append(Node(u, dist[i]))
        # print(u, v, dist[i])
     # print("Weight of MST: {0}".format(ans))


def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


c, s, q = map(int, input().split())
count = 1
flag = False

while c != 0 or s != 0 or q != 0:
    graph = [[] for i in range(c + 1)]
    dist = [INF for i in range(c + 1)]
    path = [-1 for i in range(c + 1)]
    visited = [False for i in range(c + 1)]

    visited_res = [False] * 105
    path_res = [0] * 105
    graph_res = [[] for i in range(105)]

    for i in range(s):
        c1, c2, d = map(int, input().split())
        graph[c1].append(Node(c2, d))
        graph[c2].append(Node(c1,d))

    for i in range(1,c+1):
        if not visited[i]:
            Prim(i)
    printMST()

    if flag:
        print()

    flag = True
    print("Case #{}".format(count))
    for i in range(q):
        c1, c2 = map(int, input().split())
        DFS(c1)
        printPath(c1, c2, path_res)

    count += 1
    c, s, q = map(int, input().split())

