n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
result = 0

for i in range(len(arr)):
    if x < 1:
        x = 1
    result += arr[i] * x
    x -= 1

print(result)