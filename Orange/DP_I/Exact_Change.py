def coin_change(total, coins, n, item_price, result):    
    for i in range(n): 
        for j in range(total, coins[i]-1, -1): 
            result[j] = min(result[j], result[j - coins[i]] + 1) 

    for i in range(item_price, total+1):
        if result[i] < INF: 
            return i, result[i]
    return result[i]


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        item_price = int(input())
        num_of_coins = int(input())
        coins_arr = []
        for j in range(num_of_coins): 
            coin = int(input())
            coins_arr.append(coin)
            
        sum_coin = sum(coins_arr)  
        INF = int(1e9)
        result = [INF] * (sum_coin + 1)
        result[0] = 0
        
        res = coin_change(sum_coin, coins_arr, num_of_coins, item_price, result)
        print(*res)
