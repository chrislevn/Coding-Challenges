class Node: 
    def __init__(self, id, distance, priority): 
        self.id = id
        self.distance = distance
        self.priority = priority

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.distance, self.priority)
        

sample_graph = [[[0, 1], 10], 
                [[1, 2], 4], 
                [[0, 2], 5], 
                [[0, 3], 1], 
                [[2, 5], 6], 
                [[1, 4], 19], 
                [[1, 6], 2], 
                [[4, 8], 7], 
                [[5, 7], 9], 
                [[4, 7], 11], 
                [[2, 4], 8], 
                [[4, 5], 8]]

sample_priority = [0, 1, 0, 0, 7, 3, 0, 4, 3]
sample_dest = [1, 4, 5, 7, 8]

graph = []

import queue 

MAX = 100 
INF = int(1e9)

def Dijkstra(s): 

    # Create a priority queue to store vertex and cost value 
    # of unchecked vertexes but connected to current vertex
    # follow by (x, y) where x is vertex and y is cost
    pq = queue.Queue()

    # Start from source 
    pq.put(Node(s, 0, 0))
    dist[s] = 0

    while pq.empty() == False: 
        top = pq.get()
        u = top.id      # vertex
        w = top.distance    # cost
        pr = top.priority

        for neighbor in graph[u]: 
            # Comparation
            if w + neighbor.distance - neighbor.priority < dist[neighbor.id]: 
                dist[neighbor.id] = w + neighbor.distance - neighbor.priority
                pq.put(Node(neighbor.id, dist[neighbor.id], neighbor.priority))
                path[neighbor.id] = u

# Print path method without recursion
def printPath(s, f): 
    finalPath = []
    b = []
    if s == f: 
        print(s)
        return 

    if path[f] == -1: 
        print("No path")
        return 

    while True: 
        b.append(f)
        f = path[f]
        if f == s: 
            b.append(s)
            break 

    for i in range(len(b)-1, -1, -1): 
        print(b[i], end= ' ')
        finalPath.append(b[i])

    return finalPath


def calcutePriority(s, f): 
    pathCost = printPath(s, f)
    sumPriority = 0
    for i in pathCost: 
        sumPriority += sample_priority[i]
    return sumPriority


if __name__ == '__main__': 
    n = len(sample_priority)
    # n + 5 is to ensure capicity 
    graph = [[] for i in range(n + 5)]

    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]


    for i in range(len(sample_graph)): 
        curr_node = sample_graph[i]
        source, dest = curr_node[0][0], curr_node[0][1]
        distance = curr_node[1]
        priority_source = sample_priority[source]
        priority_dest = sample_priority[dest]

        graph[source].append(Node(dest, distance, priority_dest))
        graph[dest].append(Node(source, distance, priority_dest))

    # for i in graph: 
    #     for j in i: 
    #         print(j)
    
    Dijkstra(0)
    for i in sample_dest: 
        printPath(0, i)
        print("|| dist: {} - cost: {}".format(dist[i], calcutePriority(0, i)))
        print()
        # print(i, dist[i])
    # print(ans)



