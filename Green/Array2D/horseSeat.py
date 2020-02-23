m, n = map(int, input().split())
arr = []
count = 0


for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

rez = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

for x in range(len(arr)):
    max_num = max(arr[x])
