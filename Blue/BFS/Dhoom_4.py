from queue import Queue

MAX = 100000 + 5
mod = 100000


def bfs(s, f):
    distance = [-1] * MAX
    q = Queue()
    q.put(s)
    distance[s] = 0

    while not q.empty():
        u = q.get()

        for i in arr:
            v = (i * u) % mod

            if distance[v] == -1:
                distance[v] = distance[u] + 1
                q.put(v)

                if v == f:
                    return distance[v]
    return -1


s, f = map(int, input().split())
n = int(input())
arr = list(map(int, input().split()))
print(bfs(s, f))