import math
import sys

sys.setrecursionlimit(10**6)

n = int(input())
array = list(map(int, input().split()))

def isPrime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False

        return True
    else:
        return False


def first_prime(n):
    if n < len(array):
        if isPrime(array[n]):
            return n
    if n > len(array):
        return -1
    return first_prime( n + 1)


print(first_prime(0))
