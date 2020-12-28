f = [2 ** i for i in range(64)]
a = []
s = set()
n = 0
visited = []
trace = [0] * 10

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(step, x, y):
    global f, a, s, visited
    visited[x][y] = True
    trace[step] = x * n + y

    if step == 8:
        sum = 0
        for i in range(1, 9):
            sum = sum | f[trace[i]]
        s.add(sum)
        return

    for i in range(4):
        nxtx = x + dx[i]
        nxty = y + dy[i]
        if nxtx in range(n) and nxty in range(n) and visited[nxtx][nxty] == False:
            DFS(step + 1, nxtx, nxty)
            visited[nxtx][nxty] = False

def main():
    global a, s, visited, n
    test = int(input())
    for t in range(test):
        n = int(input())

        a = []
        for i in range(n):
            a.append(input())

        s = set()

        visited = [[False] * n for i in range(n)]

        for i in range(n):
            for j in range(n):
                if a[i][j] == '.':
                    visited[i][j] = True

        for i in range(n):
            for j in range(n):
                if visited[i][j] == False:
                    DFS(1, i, j)
                    visited[i][j] = False

        print(len(s))

if __name__ == '__main__':
    main()

