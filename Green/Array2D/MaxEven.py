m, n = map(int, input().split())
arr = []
count = 0

for a in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

rez = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


for x in range(len(rez)):
    count = 0
    for y in range(len(rez[x])):
        if check_even(rez[x][y]):
            count += 1
            if count == len(rez[x]):
                print(x)
                exit()
        else:
            continue
