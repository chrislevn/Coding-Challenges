m, n, k = map(int,input().split())

arr_m = list(map(int, input().split()))
arr_n = list(map(int, input().split()))

arr = []
for i in arr_m: 
    arr.append(i)

for i in arr_n: 
    arr.append(i)

arr = sorted(arr)

print(arr[k])
