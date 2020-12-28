import queue 

def topological_sort(graph, result): 
    indegree = [0] * (V+1)
    zero_indegree = queue.PriorityQueue()
    for u in range(1, V+1): 
        for v in graph[u]: 
            indegree[v] += 1
    
    for i in range(1, V+1): 
        if indegree[i] == 0: 
            zero_indegree.put(i)
    
    while not zero_indegree.empty(): 
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                zero_indegree.put(v)

    for i in range(1, V+1): 
        if indegree[i] != 0: 
            return False

    return True


if __name__ == "__main__": 
    V, E = map(int, input().split())
    graph = [[] for i in range(V+5)]
    result = []

    for i in range(E): 
        u, v = map(int, input().split())
        graph[u].append(v)

    if (topological_sort(graph, result)): 
        for i in range(V): 
            print(result[i], end = ' ')
    
    else: 
        print('Sandro fails.')