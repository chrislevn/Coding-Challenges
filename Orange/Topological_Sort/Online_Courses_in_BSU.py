import queue 
import sys

sys.setrecursionlimit(int(10e5))

MAX = int(10e5 + 1000)

visited = [0] * (MAX)
indegree = [0] * (MAX)
topo = [0] * (MAX)
a = [0] * MAX

graph = [[] for i in range(MAX)]
result = []

q = queue.Queue()

flag = True

def dfs(u): 
    visited[u] = 1
    for v in graph[u]: 
        if visited[v] == 0:    #root
            visited[v] = 1
            dfs(v)
        else: 
            if visited[v] == 1: #pre-root
                print(-1)
                exit()
            elif visited[v] == 2: 
                continue # already visited
    visited[u] = 2
    result.append(u)



n, k = map(int, input().split())

arr_k = list(map(int, input().split())) #read_k
for item in arr_k: 
    a[item] = 1

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    if arr[0] != 0: 
        for j in range(1, len(arr)): 
            graph[i].append(arr[j])

for u in range(1, n+1): 
    if a[u] == 1 and visited[u] == 0:
        dfs(u)
    if not flag: 
        print(-1)
        exit() 

print(len(result))
for idx in range(len(result)):
    print(result[idx], end=' ')  
