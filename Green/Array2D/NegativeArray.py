m, n = map(int, input().split())
arr = []

for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

rez = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

for x in range(len(rez)):
    for y in range(len(rez[x])):
        if rez[x][y] >= 0:
            break
        else:
            if y == len(rez[x]) - 1:
                print(x, end=' ')
