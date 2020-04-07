def binarySearch(a, left, right, x):
    while (left <= right):
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    count = 0

    moneyArr = list(map(int, input().split()))

    moneyArr = sorted(moneyArr)
    for j in range(len(moneyArr)):
        findValue = m - moneyArr[j]
        res = binarySearch(moneyArr, j + 1, len(moneyArr) - 1, findValue)
        if res != -1:
            count += 1
    print(count)
