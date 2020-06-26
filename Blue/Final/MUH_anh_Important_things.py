n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = (arr[i], i + 1)

arr = sorted(arr)
swaps = []

for i in range(1, n):
    if arr[i][0] == arr[i-1][0]:
        swaps.append((i-1, i))
    if len(swaps) >= 2:
        break

if len(swaps) < 2:
    print("NO")
else:
    print("YES")
    array_index = []
    for i in range(len(arr)):
        array_index.append(arr[i][1])

    print(*array_index)

    array_index[swaps[0][0]], array_index[swaps[0][1]] = array_index[swaps[0][1]], array_index[swaps[0][0]]
    print(*array_index)

    array_index[swaps[1][0]], array_index[swaps[1][1]] = array_index[swaps[1][1]], array_index[swaps[1][0]]
    print(*array_index)
