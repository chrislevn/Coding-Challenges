import math

m, n = map(int, input().split())
arr = []
border_arr = []
count = 0
#
for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)


def check_primary(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False

        return True
    else:
        return False


rez = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
border_arr.append(arr[0])
border_arr.append(arr[-1])
border_arr.append(rez[0][1:len(rez[0]) - 1])
border_arr.append(rez[-1][1:len(rez[-1]) - 1])

for i in range(len(border_arr)):
    for j in range(len(border_arr[i])):
        if check_primary(border_arr[i][j]):
            count += 1
print(count)
