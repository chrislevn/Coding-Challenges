n = int(input())
arr = list(map(int, input().split()))

def checkFashion(array):
    count_0 = 0
    if (len(array) == 1):
        if (array[0] == 1):
            print("YES")
            return
        else:
            print("NO")
            return

    for i in range(len(array)):
        if (array[i] == 0):
            count_0 += 1

    if (count_0 > 1) | (count_0 == 0):
        print("NO")
    else:
        print("YES")


checkFashion(arr)