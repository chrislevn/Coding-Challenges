import math

n = int(input())

def check_max_odd(num, divisor):
    if divisor % 2 == 1 and num % divisor == 0:
        return int(divisor)
    return check_max_odd(num, divisor // 2)

print(check_max_odd(n, n))