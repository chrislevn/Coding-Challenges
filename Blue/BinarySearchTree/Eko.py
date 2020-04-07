def BS_search(l, r, M, arr):
    ans = r
    while l <= r:
        mid = int((l + r) / 2)
        if findRemain(arr, mid) >= M:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


def findRemain(a, x):
    sumValue = 0
    for i in range(len(a)):
        if a[i] > x:
            sumValue += a[i] - x
    return sumValue


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
maxValue = arr[-1]


res = BS_search(0, maxValue, m, arr)
print(res)

