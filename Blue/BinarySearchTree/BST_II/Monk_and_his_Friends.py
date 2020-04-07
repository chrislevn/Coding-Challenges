t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    mArr = arr[n:]
    nArr = set(arr[:n])

    for j in range(len(mArr)):
        if mArr[j] in nArr:
            print("YES")
        else:
            print("NO")
        nArr.add(mArr[j])