def solve(total, coins, n): 
    result = [0] * (total + 1)
    result[0] = 1
    
    for i in range(n): 
        for j in range(coins[i], total + 1): 
            result[j] += result[j - coins[i]]
    
    return result

if __name__ == '__main__': 
    
    MAX_VALUE = 10000
    result = [1] * MAX_VALUE     
    max_temp = 1
    coins = [pow(x, 3) for x in range(1, MAX_VALUE+1)]
    final_result = solve(MAX_VALUE, coins, len(coins))
    
    while True:
        try: 
            n = int(input())
            print(final_result[n])
        except EOFError: 
            break
            