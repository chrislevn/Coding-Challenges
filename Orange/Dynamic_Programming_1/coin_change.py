def coin_change(total, coins, n): 
    result = [0] * (total + 1)
    result[0] = 1
    
    for i in range(n): 
        for j in range(coins[i], total + 1): 
            result[j] += result[j - coins[i]]
    
    return result[total]

