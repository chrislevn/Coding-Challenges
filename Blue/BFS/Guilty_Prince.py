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


def BFS(s):
    count = 1

    q = Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                count += 1
                q.put(Cell(r, c))

    return count


T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    s = Cell(0, 0)

    entrance = []

    for j in range(m):
        maze[j] = input()

        for h in range(n):
            if maze[j][h] == '@':
                s = Cell(j, h)

    for j in range(m):
        for l in range(n):
            visited[j][l] = False

            if (maze[j][l] == '.') and (j == 0 or l == 0 or j == m - 1 or l == n - 1):
                entrance.append(Cell(j, l))


    print("Case " + str(i+1) + ": " + str(BFS(s)))
