n, k = map(int, input().split())
max_arr = [0] * n
min_arr = [0] * n 
for i in range(k): 
    r = int(input())
    max_arr[i] = r
    min_arr[i] = r

for i in range(k, n):
    max_arr[i] = 3

for i in range(k, n):
    min_arr[i] = -3

print(sum(min_arr)/n, sum(max_arr)/n)