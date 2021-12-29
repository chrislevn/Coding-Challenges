INF = 1e9 
MAX = 105

class Edge: 
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def BellmanFord(s): 
    dist[s] = 0
    for i in range(1, n): 
        for j in range(m): 
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight 
            
            # if dist[u] = INF then u is not connected to the graph
            if (dist[u] != INF) and (dist[u] + w < dist[v]): 
                # update new dist with lower cost
                dist[v] = dist[u] + w
                # update path 
                path[v] = u

    # Detect negative-weight cycle
    for i in range(m): 
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight 

        if (dist[u] != INF) and (dist[u] + w < dist[v]): 
            return False 
        
    return True

if __name__ == '__main__': 
    n, m = map(int, input().split())

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w))

    s, t = 0, 4
    result = BellmanFord(s)

    if not result: 
        print("Graph containes negative weight cycle")
    else: 
        print(dist[t])

