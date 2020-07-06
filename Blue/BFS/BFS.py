from queue import Queue 

MAX = 100

V = None
E = None 

# Visited array to store visited vertex
visited = [False for i in range(MAX)]

# Path array to store connected path
path = [0 for i in range(MAX)]

# Graph array to store the list of connected vertexes
graph = [[] for i in range(MAX)]

def BFS(source): 
    # Make all vertexes unvisited first
    for i in range(V): 
        visited[i] = False 
        path[i] = -1 

    # Create a queue to store visited vertexes but not checked
    q = Queue()
    visited[s] = True # Mark source vertex as visisted
    q.put(source)


    while not q.empty(): 
        # Remove checked vertex from queue
        u = q.get()
        for v in graph[u]:
            # Add new vertexs if they are not checked but connected
            # to current vertex 
            if not visited[v]: 
                visited[v] = True
                q.put(v)
                path[v] = u


# Print path method without recursion
def printPath(s, f): 
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

# Print path method with recursion
def printPathRecursion(s, f): 
    if s == f: 
        print(f, end=' ')
    else: 
        if path[f] == -1: 
            print("No path")
        else: 
            printPathRecursion(s, path[f])
            print(f, end=' ')


if __name__ == '__main__': 
    V, E = map(int, input().split())
    for i in range(E): 
        # Importing graph (edge list)
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = 0 # example source
    f = 5 # example end 

    BFS(s)
    printPath(s, f)