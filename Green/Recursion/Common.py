import sys
import math

sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())
new_arr = []
min_num = min(a, b)

for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        new_arr.append(i)

print(max(new_arr))


# def gcd(first, second):
#     divisor = first % second
#     if divisor == 0:
#         return a
#     elif divisor == 1:
#         return 1
#     else:
#         return gcd(second, divisor)
#
#
# print(gcd(a, b))
#