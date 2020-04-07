def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


n, q = map(int, input().split())
count = 1

while n != 0 and q != 0:
    arr = []

    print("CASE# " + str(count) + ":")

    for i in range(n):
        data = int(input())
        arr.append(data)

    arr = sorted(arr)

    for i in range(q):
        findValue = int(input())
        res = bsFirst(arr, 0, len(arr) - 1, findValue)
        if res != -1:
            print(str(findValue) + " found at " + str(res + 1))
        else:
            print(str(findValue) + " not found")

    count += 1
    n, q = map(int, input().split())