def fibonacci(n): 
    if n <=1: 
        return n 
    if result[n] != 0: 
        return result[n]
    else: 
        result[n] = fibonacci(n-1) + fibonacci(n-2)
        return result[n]


if __name__ == '__main__': 
    n = 6
    result = [0] * (n+1)
    result[0] = 0
    result[1] = 1
    print(fibonacci(n))