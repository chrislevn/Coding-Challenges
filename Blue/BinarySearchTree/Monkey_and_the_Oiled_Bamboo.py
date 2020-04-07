def BS_search(l, r, stepArr):
    ans = r
    while l <= r:
        mid = int((l + r) / 2)
        if check(stepArr, mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

def check(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            k -= 1
        else:
            if arr[i] < k:
                continue
            return False
    return True


t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    stepArr = [arr[0] - 0]

    for j in range(1, len(arr)):
        stepArr.append(arr[j] - arr[j-1])

    res = BS_search(0, max(arr), stepArr)
    print("Case " + str(i + 1) + ": " + str(res))
