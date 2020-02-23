from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

new_arr = Counter(arr)
count_arr = []
length = len(new_arr)

for i in new_arr:
    count_arr.append(new_arr[i])

max_tower = max(count_arr)

print(max_tower, length)
