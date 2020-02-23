import math

m, n = map(int, input().split())
arr = []
new_arr = []
count = 0

for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

for x in range(len(arr)):
    for y in range(len(arr[x])):
        if x == y:
            new_arr.append(arr[x][y])


def check_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
            else:
                return False
    else:
        return False


for d in range(len(new_arr)):
    if check_prime(new_arr[d]):
        count += 1

print(count)
