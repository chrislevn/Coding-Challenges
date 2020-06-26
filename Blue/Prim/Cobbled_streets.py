import queue

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
    ans = 0
    for i in range(1, n+1):
        if path[i] == -1:
            continue
        ans += dist[i]
        # print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print(ans)


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


if __name__ == "__main__":

    t = int(input())
    for i in range(t):

        p = int(input())
        n = int(input())
        m = int(input())

        graph = [[] for i in range(n + 1)]
        dist = [INF for i in range(n + 1)]
        path = [-1 for i in range(n + 1)]
        visited = [False for i in range(n + 1)]

        for j in range(m):
            a, b, c = map(int, input().split())
            c *= p
            graph[a].append(Node(b, c))
            graph[b].append(Node(a, c))

        Prim(1)
        printMST()
