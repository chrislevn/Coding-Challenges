n = int(input())
arr = []


for i in range(n):
    number = str(input())
    arr.append(number)

repeat = arr[0]
count = 1

for i in range(1, len(arr)):
    if arr[i] != repeat:
        count += 1
    repeat = arr[i]

print(count)