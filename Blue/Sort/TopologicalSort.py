# A recursive function used by topologicalSort 
def topologicalSortUtil(self,v,visited,stack): 

    # Mark the current node as visited. 
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex 
    for i in self.graph[v]: 
        if visited[i] == False: 
            self.topologicalSortUtil(i,visited,stack) 

    # Push current vertex to stack which stores result 
    stack.insert(0,v) 

# The function to do Topological Sort. It uses recursive  
# topologicalSortUtil() 
def topologicalSort(self): 
    # Mark all the vertices as not visited 
    visited = [False]*self.V 
    stack =[] 

    # Call the recursive helper function to store Topological 
    # Sort starting from all vertices one by one 
    for i in range(self.V): 
        if visited[i] == False: 
            self.topologicalSortUtil(i,visited,stack) 

    # Print contents of stack 
    print stack



if __name__ == '__main__': 
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    