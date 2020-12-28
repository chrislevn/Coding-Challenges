import queue 

def topological_sort(graph, result): 
    indegree = [0] * V
    zero_indegree = queue.PriorityQueue()
    for u in range(V): 
        for v in graph[u]: 
            indegree[v] += 1
    
    for i in range(V): 
        if indegree[i] == 0: 
            zero_indegree.put(i)
    
    while not zero_indegree.empty(): 
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                zero_indegree.put(v)

    for i in range(V): 
        if indegree[i] != 0: 
            return False

    return True


if __name__ == "__main__":
    case = 1

    while True: 
        n = int(input())
        V = n
        beverage_arr = []
        graph = [[] for i in range(V+5)]
        result = []


        for i in range(n): 
            beverage = input()
            beverage_arr.append(beverage)

        m = int(input())
        E = m
        for i in range(m): 
            u, v = map(str, input().split())
            graph[beverage_arr.index(u)].append(beverage_arr.index(v))

        if (topological_sort(graph, result)): 
            print('Case #' + str(case) + ': Dilbert should drink beverages in this order: ', end=' ') 
            for i in range(V-1):
                print(beverage_arr[result[i]], end = ' ')
            
            print(beverage_arr[result[V-1]] + '.')

    
        try: 

            empty = input()
            case += 1

        except EOFError:
            break 

        print()