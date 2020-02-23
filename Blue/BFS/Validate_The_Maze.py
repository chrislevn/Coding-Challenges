from queue import Queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 21
visited = [[False] * MAX for i in range(MAX)]
maze = [None] * MAX


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
        if u.r == f.r and u.c == f.c:
            return True

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))

    return False

T = int(input())

for i in range(T):
    m, n = map(int, input().split())

    for j in range(m):
        maze[j] = input()

    entrance = []

    for j in range(m):
        for l in range(n):
            visited[j][l] = False

            if (maze[j][l] == '.') and (j == 0 or l == 0 or j == m - 1 or l == n - 1):
                entrance.append(Cell(j, l))

    if (len(entrance)) != 2:
        print("invalid")
    else:
        s = entrance[0]
        f = entrance[1]

        if BFS(s, f):
            print("valid")
        else:
            print("invalid")






