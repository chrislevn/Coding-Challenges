import sys
sys.setrecursionlimit(10000000)
count = 0 

def dfs(graph, start_time, finsih_time, v): 
    global count
    count += 1
    start_time[v] = count
    for u in graph[v]: 
        if start_time[u] == 0: 
            dfs(graph, start_time, finsih_time, u)
    finish_time[v] = count


if __name__ == "__main__": 
    n = int(input())
    graph = [[] for i in range(n)]
    
    for i in range(n - 1): 
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        
        graph[a].append(b)
        graph[b].append(a)
        
    start_time = [0] * n 
    finish_time = [0] * n 
    dfs(graph, start_time, finish_time, 0)
        
    q = int(input())
    for i in range(q): 
        direction, x, y = map(int, input().split())
        x -= 1
        y -= 1
        
        if direction == 0: 
            if start_time[x] <= start_time[y] and start_time[y] <= finish_time[x]: 
                print("YES")
            else: 
                print("NO")
        else: 
            if start_time[y] <= start_time[x] and start_time[x] <= finish_time[y]: 
                print("YES")
            else: 
                print("NO")
            