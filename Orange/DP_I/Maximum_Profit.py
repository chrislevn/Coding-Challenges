def max_profit(prices, n, k): 
    """
    Get maximum profit of stock prices
    
    Args: 
        prices (list): list of input prices
        n (int): length of prices array or days
        k (int): number of allowed transactions 
        
    Returns: 
        max_profit_result (int): max profit
    
    """

    profit = [[0 for i in range(k + 1)] for j in range(n + 1)]
    
    for i in range(1, n):
        for j in range(1, k + 1): 
            max_temp = 0
            for l in range(i): 
                max_temp = max(max_temp, prices[i] - prices[l] + profit[l][j-1])
            profit[i][j] = max(profit[i-1][j], max_temp)
    
    return profit[n-1][k]    

if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        k = int(input())
        n = int(input()) 
        arr = list(map(int, input().split()))
                
        print(max_profit(arr, n, k))
            