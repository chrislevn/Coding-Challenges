MAX = 100
visited = [[False] * MAX for i in range(MAX)]
patternFound = False
pattern = "ALLIZZWELL"


def isValid(x, y, r, c):
    if (x >= 0) and (x < r) and (y >= 0) and (y < c):
        return True
    return False


def findPattern(x, y, r, c, idx):
    #print(x, y, idx)
    global patternFound
    if idx == 9:
        patternFound = True
        return

    visited[x][y] = True
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, 1, -1, 1, -1]

    i = 0
    while i < 8 and not patternFound:
        nextX = x + dr[i]
        nextY = y + dc[i]

        if isValid(nextX, nextY, r, c) and not visited[nextX][nextY] and letter_arr[nextX][nextY] == pattern[idx + 1]:
            findPattern(nextX, nextY, r, c, idx + 1)
        i += 1
    visited[x][y] = False


t = int(input())
for i in range(t):
    r, c = map(int, input().split())

    letter_arr = []
    patternFound = False

    for j in range(r):
        letters = list(input())
        letter_arr.append(letters)
    space = input()
    #print(*letter_arr, sep = "\n")
    for j in range(len(letter_arr)):
        for l in range(len(letter_arr[j])):
            #print(letter_arr[j][l], sep = ' ')
            if letter_arr[j][l] == "A":
                findPattern(j, l, r, c, 0)
                if patternFound:
                    break
        if patternFound:
            break
    if patternFound:
        print("YES")
    else:
        print("NO")

