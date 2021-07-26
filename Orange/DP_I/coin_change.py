def coin_change(total, coins, n): 
    result = [0] * (total + 1)
    result[0] = 1
    
    for i in range(n): 
        for j in range(coins[i], total + 1): 
            result[j] += result[j - coins[i]]
    
    return result[total]

def print_solution(result, total, coins, n, pos): 
    if total == 0: 
        for r in result: 
            print(r, end= ' ')
        print()
    for i in range(pos, n):
        if total >= coins[i]: 
            result.append(coins[i])
            print_solution(result, total - coins[i], n, i)
            result.pop()