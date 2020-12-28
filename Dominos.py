from collections import deque
 
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {i: [] for i in range(self.vertices)}
 
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
 
    def BFS(self, u):
        visited = [False for i in range(self.vertices + 1)]
        distance = [-1 for i in range(self.vertices + 1)]
 
        distance[u] = 0
        queue = deque()
        queue.append(u)
        visited[u] = True
 
        while queue:
 
            front = queue.popleft()
 
            for i in self.adj[front]:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[front]+1
                    queue.append(i)
 
        maxDis = 0
 
        for i in range(self.vertices):
            if distance[i] > maxDis:
 
                maxDis = distance[i]
                nodeIdx = i
 
        return nodeIdx, maxDis
 
    def LongestPathLength(self): 
        node, Dis = self.BFS(1)
 
        node_2, LongDis = self.BFS(node)
 
        print(LongDis)

tile = input()
G = Graph(10)

while tile !=  "-1":
    a, b = map(int, tile.split(" "))
    a, b = int(a), int(b)
    G.addEdge(a, b)
    
    tile = input()

G.LongestPathLength()