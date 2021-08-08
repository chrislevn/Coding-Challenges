import math 


class Coin: 
    def __init__(self, conventional_value, info_value):
        self.conv = conventional_value
        self.info = info_value
 
 
def calc_ecoin(conv, info): 
    return math.sqrt(math.pow(conv, 2) + math.pow(info, 2)) 
      

def coin_change(total, coins, n): 
    global dp
    
    for i in range(total + 1): 
        for j in range(total + 1): 
            if i == 0 and j == 0: 
                continue
            dp[i][j] = 1e9
            for k in range(n): 
                if i >= coins[k].conv and j >= coins[k].info: 
                    dp[i][j] = min(dp[i][j], dp[i - coins[k].conv][j - coins[k].info] + 1)
    return dp


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


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        space = input()
        m, s = map(int, input().split())
        dp = [[1e9 for i in range(s+1)] for j in range(s+1)]
        dp[0][0] = 0
        arr = []
        for j in range(m): 
            conv, info = map(int, input().split())
            arr.append(Coin(conv, info))
        
        result_dp = coin_change(s, arr, m)
        ans = 1e9
        
        temp_arr = []
        for i in range(s+1): 
            info_temp = i
            conv_temp = int(math.sqrt(math.pow(s, 2) - math.pow(info_temp, 2)))
            if (math.pow(conv_temp, 2) == math.pow(s, 2) - math.pow(info_temp, 2)): 
                ans = min(ans, result_dp[conv_temp][info_temp])
            
        if ans == 1e9: 
            print("not possible")
        else: 
            print(ans)
            
