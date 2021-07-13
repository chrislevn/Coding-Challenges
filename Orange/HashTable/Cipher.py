
if __name__ == "__main__": 
    n, k = map(int, input().split())
    s = input()
    result = []
    prefix = 0
    sum_xor = 0 
    
    for i in range(n): 
        if i >= k: 
            prefix ^= result[i-k]
        curr = prefix ^ int(s[i])
        prefix ^= curr
        result.append(curr)
        
    print(''.join(map(str, result)))
   