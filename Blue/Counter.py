from collections import Counter as co

arr = [2, 2, 1]
arr = co(arr)

for i in arr:
    if arr[i] == 1:
        print(i)