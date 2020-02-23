n = int(input())
arr = []

for i in range(n):
    name = input()
    name = name.lower()

    a = name.split()

    for j in a:
        upper_first = j[0].upper()
        arr.append(upper_first + j[1:])

    print(*arr)
    arr.clear()

