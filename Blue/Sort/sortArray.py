n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

l, r = 0, len(arr) - 1

new_arr = []
sub_arr = []

flag = False

while l < abs(r):
    # print("l", l)
    # print(sorted_arr[l])
    if arr[l] != sorted_arr[l]:
        sub_arr.append(l)
        break
    l += 1

while r > 0:
    # print("r", r)
    # print(sorted_arr[r])
    if arr[r] != sorted_arr[r]:
        sub_arr.append(r)
        break
    r -= 1

if l == len(arr) - 1 and r == 0:
    print("yes")
    print(1, 1)
    exit()

reverse_sub = arr[sub_arr[0]:sub_arr[1] + 1]
reverse_sub.reverse()

if reverse_sub == sorted_arr[sub_arr[0]:sub_arr[1] + 1]:
    print("yes")
    sub_arr[0] += 1
    sub_arr[1] += 1
    print(*sub_arr)
else:
    print("no")
