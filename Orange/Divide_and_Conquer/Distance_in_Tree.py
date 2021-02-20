from queue import Queue

def DFS(s, k):
    num_pair_with_distance[s][0] = 1
    visited[s] = True
    for v in tree[s]: 
        if not visited[v]: 
            visited[v] = True 
            DFS(v, k)
            for j in range(k): 
                result[s] += num_pair_with_distance[s][j] * num_pair_with_distance[v][k-j-1]
            for j in range(1, k+1): 
                num_pair_with_distance[s][j] += num_pair_with_distance[v][j-1]
            result[s] += result[v]


if __name__ == "__main__":
    n, k = map(int, input().split())

    tree = [[] for i in range(n+5)]
    visited = [False for i in range(n+5)]
    path = [0 for i in range(n+5)]
    num_pair_with_distance = [[0] * (k+1) for i in range(n+1)]
    result = [0] * (n+1)

    for i in range(n-1): 
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    DFS(1, k)
    print(result[1])
    