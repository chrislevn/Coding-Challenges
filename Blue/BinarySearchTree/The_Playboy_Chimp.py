def BS_search_right(l, r, M, arr):
    ans = r
    while l <= r:
        mid = int((l + r) / 2)
        if arr[mid] > M:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

def BS_search_left(l, r, M, arr):
    ans = r
    while l <= r:
        mid = int((l + r) / 2)
        if arr[mid] < M:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


n = int(input())
nArr = list(map(int, input().split()))
nArr = sorted(nArr)
maxN = nArr[-1]
minN = nArr[0]

q = int(input())
qArr = list(map(int, input().split()))

for i in range(len(qArr)):
    # resultArr = []
    resLeft = BS_search_left(0, len(nArr) - 1, qArr[i], nArr)
    resRight = BS_search_right(0, len(nArr) - 1, qArr[i], nArr)

    lower = nArr[resLeft]
    higher = nArr[resRight]

    if lower >= qArr[i]:
        lower = 'X'
    if higher <= qArr[i]:
        higher = 'X'

    print(lower, higher)
