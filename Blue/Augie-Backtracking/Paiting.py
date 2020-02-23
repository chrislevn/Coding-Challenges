arr = list(input().split(","))
n = int(input())
result = []

arr[0] = arr[0].split("[")[1]
arr[-1] = arr[-1].split("]")[0]

for i in range(len(arr)):
    arr[i] = int(arr[i])

for i in range(len(arr) - 1):
    if arr[i] + arr[i+1] == n:
        result.append(i)
        result.append(i+1)
        break

print("[" + str(result[0]) + "," + str(result[1]) + "]")
