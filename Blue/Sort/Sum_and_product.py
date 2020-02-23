n = int(input())
arr = list(map(int, input().split()))

one_arr = []

for i in range(len(arr)):
    if arr[i] == 1:
        one_arr.append(1)
    else:
        one_arr.append(0)

sum_sub = []
pro_sub = []
count_sum = 0

for i in range(len(arr)):
    if arr[i] is not 1:
        count_sum += arr[i]
    else:
        sum_sub.append(count_sum)
        count_sum = 0



print("sub_sum", sum_sub)
print(one_arr)