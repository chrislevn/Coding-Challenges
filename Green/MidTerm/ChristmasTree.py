n = int(input())
count = 0
count_space = n
arr = []

for i in range(n):

    count = 2 * i + 1
    count_space -= 1

    for m in range(count_space):
        arr.append(" ")

    for j in range(count):
        arr.append("*")

    print(*arr, sep="")
    arr.clear()
