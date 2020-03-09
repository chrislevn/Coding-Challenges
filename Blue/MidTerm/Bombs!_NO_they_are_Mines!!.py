from queue import Queue


class Cell:
    def __init__(self, row=0, col=1):
        self.r = row
        self.c = col


def isValid(r, c):
    return r in range(m) and c in range(n)


def BFS(s, f):
    q = Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        # print(u.r, u.c)
        if u.r == f.r and u.c == f.c:
            break
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c) and table[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                dist[r][c] = dist[u.r][u.c] + 1

    return dist[f.r][f.c]


m, n = map(int, input().split())

while (m != 0) and (n != 0):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    MAX = 1005
    visited = [[False] * MAX for i in range(MAX)]
    dist = [[0] * MAX for i in range(MAX)]
    table = [[0] * MAX for i in range(MAX)]

    rowBomb = int(input())

    for i in range(rowBomb):
        arr = list(map(int, input().split()))
        row, bomb = arr[0], arr[1]

        newArr = arr[2:len(arr)]

        for col in newArr:
            table[row][col] = 1

    rowStart, colStart = map(int, input().split())

    s = Cell(rowStart, colStart)

    rowNext, colNext = map(int, input().split())

    f = Cell(rowNext, colNext)

    print(BFS(s, f))

    m, n = map(int, input().split())

