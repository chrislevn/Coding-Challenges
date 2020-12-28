import queue 

class Employee: 
    def __init__(self, rank, index):
        self.rank = rank
        self.index = index

    def __lt__(self, other): 
        if other.rank > self.rank: 
            return True
        elif other.rank == self.rank: 
            if other.index > self.index: 
                return True
        return False


def topological_sort(graph, result): 
    indegree = [0] * (V)
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
    T = int(input())

    for t in range(T): 
        V, E = map(int, input().split())
        graph = [[] for i in range(V+5)]
        result = []
        rank = []

        for i in range(E): 
            u, v = map(int, input().split())
            graph[v].append(u)

        print('Scenario #' + str(t+1) + ':')

        if (topological_sort(graph, result)): 
            # for i in range(V): 
            #     print(result[i], end = ' ')

            rank = [1]*len(result)
            for tmp in result: 
                for v in graph[tmp]:
                    rank[v] = max(rank[v], rank[tmp]+1)

            answer = []
            for i in range(len(rank)): 
                answer.append(Employee(rank[i], i))
            
            answer.sort()

            for i in answer:
                print(i.rank, i.index)