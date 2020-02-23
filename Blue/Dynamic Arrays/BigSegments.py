n = int(input())
left_arr, right_arr = [], []

for i in range(n):
    l, r = map(int, input().split())

    left_arr.append(l)
    right_arr.append(r)

left = min(left_arr)
right = max(right_arr)

for i in range(n):
    if left == left_arr[i] and right == right_arr[i]:
        print(i + 1)
        exit()

print(-1)






