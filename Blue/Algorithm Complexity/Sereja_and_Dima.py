n = int(input())
arr = list(map(int, input().split()))

sere = []
dima = []

left, right = 0, (n - 1)
mid = len(arr) // 2

count = 1
while count <= len(arr):
    if count % 2 != 0:
        if arr[left] < arr[right]:
            sere.append(arr[right])
            right -= 1
        else:
            sere.append(arr[left])
            left += 1

    if count % 2 == 0:
        if arr[left] < arr[right]:
            dima.append(arr[right])
            right -= 1
        else:
            dima.append(arr[left])
            left += 1

    count += 1

print(sum(sere), sum(dima))