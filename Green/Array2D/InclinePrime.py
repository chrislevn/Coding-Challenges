import math

n = int(input())
arr =[]

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

new_arr = []
count = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == j:
            new_arr.append(arr[i][j])

def check_primary(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False

        return True
    else:
        return False

for x in range(len(new_arr)):
    if check_primary(new_arr[x]):
        count += 1

print(count)


