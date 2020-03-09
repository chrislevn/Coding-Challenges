n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
print(arr[int(n / 2)])
