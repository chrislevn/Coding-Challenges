from queue import Queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 21
visited = [[False] * MAX for i in range(MAX)]
g = 1
check = [None] * MAX

def BFS(i, j, r, c):
    check[i][j] = 1

    if (i > 0) and (arr[i+1][j+1] ) == 1 and (check[i+1][j+1] == 0):
        g += 1
        BFS(i-1, j, n, m)

    if (i < n - 1) and (arr[i+1][j] == 1)  and (check[i+1][j] == 0):
        g += 1
        BFS(i+1, j, n, m)

    if (j > 0) and (arr[i][j-1] == 1) and (check[i][j-1] == 0):
        g += 1
        BFS(i, j-1, n, m)

    if (j<m-1) and (arr[i][j+1] == 1)  and (check[i][j+1] == 0):
        g += 1
        BFS(i, j+1, n, m)


while (True):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    count = 0
    arr = []
    check = []

    for x in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
        temp_check = []
        for y in range(m):
            temp_check.append(0)
        check.append(temp_check)

    for x in range(n):
        for y in range(m):
            if (arr[x][y] == 1) and (check[x][y] == 0):
                count += 1
                BFS(x, y, n, m)
    print(count)



