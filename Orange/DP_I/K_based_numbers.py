def solve(n, k): 
    S_end_0     = [0]
    S_end_not_0 = [k-1]
    
    if n >= 2: 
        for i in range(2, n+1): 
            S_end_0.append(S_end_not_0[-1])
            S_end_not_0.append((k-1) * (S_end_0[i-2] + S_end_not_0[-1]))
            
    return S_end_0[-1] + S_end_not_0[-1]
        
if __name__ == '__main__': 
    n = int(input())
    k = int(input())
    
    print(solve(n, k))
    
    