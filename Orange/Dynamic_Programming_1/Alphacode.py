def solve(n, dp):     
    for i in range(2, len(n)+1): 
        single = int(n[i-1])
        double = int(n[i-2:i])
                
        if single > 0 and single < 10:
            dp[i] += dp[i-1]
        if double > 0 and double < 27 and n[i-2] != '0':
            
            dp[i] += dp[i-2]
    return dp[-1]
        
if __name__ == '__main__': 
    n = input()
    
    while n != '0': 
        dp = [1, 1] + [0] * (len(n) - 1)
        print(solve(n, dp))
        n = input()