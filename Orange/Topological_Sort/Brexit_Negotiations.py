import queue 

MAX = int(10e5 + 1000)

class Node: 
    def __init__(self, i, j): 
        self.i = i 
        self.j = j 
    
    def __lt__(self, other): 
        return 



def topological_sort(graph, result): 
    indegree = [0] * (n+1)
    zero_indegree = queue.PriorityQueue()
    for u in range(1, n+1): 
        for v in graph[u]: 
            indegree[v] += 1
    
    for i in range(1, n+1): 
        if indegree[i] == 0: 
            zero_indegree.put(i)
    
    while not zero_indegree.empty(): 
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                zero_indegree.put(v)

    for i in range(1, n+1): 
        if indegree[i] != 0: 
            return False

    return True


if __name__ == "__main__": 
    n = int(input())

    graph = [[] for i in range(MAX)]
    result = []

    for i in range(1, n+1): 
        arr = list(map(int, input().split()))
        if arr[1] != 0:
            for j in arr[2:]: 
                graph[j].append(i)

    if (topological_sort(graph, result)):
        print(*result)
        