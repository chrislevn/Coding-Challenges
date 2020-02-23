m, n = map(int, input().split())
a, b, p = map(int, input().split())

arr = []

for x in range(m):
    temp = []
    for y in range(n):
        temp.append(0)

    arr.append(temp)

arr[0][0] = a
arr[0][1] = b

for i in range(m):
    if i == 0:
        for j in range(2, n):
            value = (a + b) % p
            a = b
            b = value

            arr[i][j] = value

        continue
    for j in range(n):
        value = (a + b) % p
        a = b
        b = value

        arr[i][j] = value
        continue

for d in range(m):
    for e in range(n):
        print(arr[d][e], end=' ')
    print( )
