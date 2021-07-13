def gcd(a, b): 
    while b != 0: 
        remainder = a % b 
        a = b 
        b = remainder
    return a 

def phi(n): 
    result = n 
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            while n % i == 0: 
                n //= i 
            result = result // i * (i - 1)
    
    if n > 1: 
        result = result // n * (n - 1)
    return result


if __name__ == "__main__": 
    n = int(input())
    while n != 0: 
        result = phi(n)
        # for i in range(n): 
        #     if gcd(i, n) == 1: 
        #         result += 1
        print(result)
        n = int(input())