from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = 0

sort_arr = sorted(arr)
count_arr = list(Counter(sort_arr).values())


for i in range(len(count_arr)):
    result += count_arr[i] * count
    count = count_arr[i] + count


print(result)
