from queue import PriorityQueue
INF = 1e9

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def primMST():
    ans = 0
    for i in range(1, count_1+1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans


def Prim(src):
    pq = PriorityQueue()
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


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        space = input()
        n = int(input())

        graph = [[] for i in range(2*n+5)]
        dist = [INF for i in range(2*n+5)]
        path = [-1 for i in range(2*n+5)]
        visited = [False for i in range(2*n+5)]

        s = dict()
        count_1 = 0

        for j in range(n):
            city_1, city_2, cost = list(input().split())
            cost = int(cost)
            if city_1 not in s:
                count_1 += 1
                s[city_1] = count_1

            if city_2 not in s:
                count_1 += 1
                s[city_2] = count_1

            city_1 = s[city_1]
            city_2 = s[city_2]

            graph[city_1].append(Node(city_2, cost))
            graph[city_2].append((Node(city_1, cost)))

        Prim(1)

        flag = True
        for a in range(1, count_1 + 1):
            if not visited[a]:
                flag = False
                break
        if flag:
            print("Case {}: {}".format(i+1, primMST()))
        else:
            print("Case {}: Impossible".format(i+1))

