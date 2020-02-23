n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
a_arr = []
b_arr = []

for i in range(a):
    a_arr.append(arr[i])

for i in range(a, n):
    b_arr.append(arr[i])


if a_arr[-1] > b_arr[0]:
    print(a_arr[-1] - b_arr[0])
else:
    print(0)