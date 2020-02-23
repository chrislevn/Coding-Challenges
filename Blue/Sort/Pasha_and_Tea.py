n, w = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

check = w / (3*n)

# if min(arr) > w:
#     print(w)
#     exit()
#
# while curr < check:
#     curr += 0.5
#     if curr > min(arr):
#         break
#
#     if 3*curr * n <= w:
#         result = curr * 3 * n

x = arr[0]
y = arr[n] / 2
curr = min(x, y)
result = 3 * curr * n

print(min(w, result))