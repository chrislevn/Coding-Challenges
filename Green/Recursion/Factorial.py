n = int(input())

def Factorial(num):
    if num < 1:
        return 1
    else:
        result = num * Factorial(num - 1)
        return result

print(Factorial(n))