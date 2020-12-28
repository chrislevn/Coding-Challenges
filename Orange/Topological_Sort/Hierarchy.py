import queue 

def hierarchy(graph, result): 
    indegree = [0] * (N+1)
    zero_indegree = queue.Queue()
    for u in range(1, N+1): 
        for v in graph[u]: 
            indegree[v] += 1
    
    for i in range(1, N+1): 
        if indegree[i] == 0: 
            zero_indegree.put(i)
    
    while not zero_indegree.empty(): 
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                zero_indegree.put(v)

    boss_arr = [[] for i in range(N+5)]

    for i in range(1,len(result)): 
        boss_arr[result[i]].append(result[i-1])
    
    for i in range(1, N+1):
        if len(boss_arr[i]) == 0: 
            print(0)
        else: 
            print(boss_arr[i][0])


if __name__ == "__main__": 
    N, K = map(int, input().split())
    graph = [[] for i in range(N+5)]
    result = []

    for i in range(1, K+1): 
        arr = list(map(int, input().split()))
        w = arr[0]
        for j in arr[1:]:
            graph[i].append(j)
    hierarchy(graph, result)