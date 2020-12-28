from queue import Queue 

limit = 10**9
mark = set()
dist = dict()

dx = [0, 0, 1, -1, 1, -1, 1, -1] 
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def calc(x, y): 
    tmp = x
    tmp = tmp*(10**9) + y
    return int(tmp)

def BFS(): 
    myQueue = Queue()
    s = calc(x0, y0) 
    myQueue.put(s)
    dist[s] = 0 

    while not myQueue.empty(): 
        u = myQueue.get()
        
        x = u // limit
        y = u % limit

        for i in range(8): 
            xx = x + dx[i]
            yy = y + dy[i]
            v = calc(xx, yy)

            if xx >= 1 and xx <= limit and yy >= 1 and yy <= limit and v in mark: 
                if v not in dist.keys(): 
                    dist[v] = dist[u] + 1
                    if v == calc(x1, y1): 
                        print(dist[v])
                        return
                    myQueue.put(v)
    print(-1)



if __name__ == "__main__": 
    x0, y0, x1, y1 = map(int, input().split()) 
    mark.add(calc(x0, y0))
    mark.add(calc(x1, y1))

    n = int(input())
    for i in range(n): 
        r, a, b = map(int, input().split())
        for j in range(a, b+1):
            mark.add(calc(r, j))

    BFS()

    

   