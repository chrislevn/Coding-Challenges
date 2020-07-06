import queue 

MAX = 100 
INF = int(1e9)

# Create node (vertex) class in which each vertex will
# carry a distance cost
class Node: 
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id 

    # compare method 
    def __lt__(self, other):
        return self.dist <= other.dist 


def Dijkstra(s): 

    # Create a priority queue to store vertex and cost value 
    # of unchecked vertexes but connected to current vertex
    # follow by (x, y) where x is vertex and y is cost
    pq = queue.PriorityQueue()

    # Start from source 
    pq.put(Node(s, 0))
    dist[s] = 0

    while pq.empty() == False: 
        top = pq.get()
        u = top.id      # vertex
        w = top.dist    # cost

        for neighbor in graph[u]: 
            # Comparation
            if w + neighbor.dist < dist[neighbor.id]: 
                dist[neighbor.id] = w + neighbor.dist   
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u 


if __name__ == '__main__': 
    n = int(input())
    s, t = 0, 4 # sample starting and ending vertex

    # n + 5 is to ensure capicity 
    graph = [[] for i in range(n + 5)]

    # dist array to store the cost from starting node
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for i in range(n): 
        d = list(map(int, input().split()))
        for j in range(n): 
            if d[j] > 0: 
                graph[j].append(Node(j, d[j]))
    
    Dijkstra(s)
    ans = dist[t]
    print(ans)
