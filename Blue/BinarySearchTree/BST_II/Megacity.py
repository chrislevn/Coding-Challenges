import math


def distance(x2, y2):
    return x2**2 + y2**2


n, s = map(int, input().split())
arr = []
people = []
sDict = dict()

for i in range(n):
    x, y, k = map(int, input().split())
    if distance(x, y) in sDict:
        sDict[distance(x, y)] += k
    else:
        sDict[distance(x, y)] = k

for i in sDict:
    arr.append(i)

arr.sort()

flag = False
index = 0

for i in arr:
    if sDict[i] + s >= 1000000:
        flag = True
        index = i
        break
    s += sDict[i]

if flag:
    print(index**0.5)
else:
    print(-1)