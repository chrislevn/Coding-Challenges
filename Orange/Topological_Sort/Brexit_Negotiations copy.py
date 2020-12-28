MOD = 1E9+7
N = 400000+5
dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,-1,1,-1,1]

class Node: 
    def __init__(self, i, j): 
        self.id = i 
        self.j = j 
    
    def __lt__(self, other): 
        return 


a = [0] * N 
times = [0] * N 
visited = [False] * N
graph = [[] for i in range(N)]
res = -10e9
extra = 0

def DFS(x): 
    if visited[x]: 
        return
    
    if not visited[x] and len(graph[x]) == 0: 
        res = max(res, extra+times[x])
        extra += 1
        visited[x] = True
        return

    visited[x] = True
    for i in range(len(graph[x])): 
        DFS(graph[x][i])

    res = max(res, extra+times[x])
    extra += 1

if __name__ == "__main__": 
    n = int(input())

    for i in range(1, n+1): 
        arr = list(map(int, input().split()))
        if arr[1] != 0:
            for j in arr[2:]: 
                graph[j].append(i)

