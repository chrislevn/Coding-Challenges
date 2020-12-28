from queue import Queue 

MAX = 10**5

# Graph array to store the list of connected vertexes
graph = [[] for i in range(MAX+5)]

def BFS_Find_Longest(s, dist): 

    distance = 0
   
    # Create a queue to store visited vertexes but not checked
    q = Queue()

    while not q.empty(): 
        # Remove checked vertex from queue
        u = q.get()

    for i in range(1, n+1): 
        dist[i] = -1
    
    dist[s] = 0 
    q.put(s)

    while not q.empty(): 
        u = q.get()

        for v in graph[u]: 
            if dist[v] == -1:
                q.put(v)
                dist[v] = dist[u] + 1
    
    i_max = s
    for i in range(1, n+1): 
        if (dist[i] > dist[i_max] and affected[i]): 
            i_max = i
    
    return i_max


if __name__ == "__main__":
    n, m, d = map(int, input().split())
    affected = [0]*(n+1)
    p_arr = list(map(int, input().split()))

    for i in range(m): 
        affected[p_arr[i]] = 1

    for i in range(1, n): 
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    dist0 = [0] * (n+1)
    dist1 = [0] * (n+1)
    distA = [0] * (n+1)
    distB = [0] * (n+1)

    u = BFS_Find_Longest(p_arr[0], dist0)
    v = BFS_Find_Longest(u, dist1)

    BFS_Find_Longest(u, distA)
    BFS_Find_Longest(v, distB)

    res = 0 
    for i in range(1, n+1):
        if distA[i] <= d and distB[i] <= d: 
            res += 1
    
    print(res)
    