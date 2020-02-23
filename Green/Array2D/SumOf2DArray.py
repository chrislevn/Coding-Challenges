m, n = map(int, input().split())
arr = []

for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

for x in range(len(arr)):
    print("{}: {}".format(x, sum(arr[x])))
