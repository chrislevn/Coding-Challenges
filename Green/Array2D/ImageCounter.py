m, n = map(int, input().split())
arr = []
count = 0

for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] > 100:
            count += 1

print(count)

