def phi(n): 
    result = n 
    max_prime = 0
    count = 0
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            count += 1
            while n % i == 0: 
                n //= i 
                max_prime = max(max_prime, i)
            result = result // i * (i - 1)
    
    if n > 1: 
        count += 1
        result = result // n * (n - 1)
        max_prime = max(max_prime, n)
    
    return max_prime if count > 1 else -1

if __name__ == "__main__": 
    n = abs(int(input()))
    while n != 0: 
        result = phi(n)
        print(result)
        n = abs(int(input()))