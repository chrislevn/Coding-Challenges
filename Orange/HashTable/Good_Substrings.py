BASE = 29

if __name__ == "__main__": 
    first = input()
    second = input()
    k = int(input())
    
    result = set()

    for i in range(len(first)): 
        hash = bad = 0 
    
        for j in range(i, -1, -1): 
            hash = hash * BASE + (ord(first[j]) - ord('a') + 1)
            if second[ord(first[j]) - ord('a')] == '0': 
                bad += 1
            
            if bad <= k:
                result.add(hash)
            else: 
                break
            
    print(len(result))
    
    
    