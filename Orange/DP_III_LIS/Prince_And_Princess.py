def lower_bound(a, sub, n, x): 
    left = 0 
    right = n 
    pos = right 
    while left < right: 
        mid = left + (right - left) // 2
        index = sub[mid]
        
        if a[index] >= x: 
            pos = mid 
            right = mid 
        else: 
            left = mid + 1
            
    return pos 

def LIS_binary_search(a): 
    global path 
    length = 1
    path = [-1] * len(a)
    result.append(0)
    
    for i in range(1, len(a)): 
        if a[i] <= a[result[0]]: 
            result[0] = i 
        elif a[i] > a[result[length - 1]]: 
            path[i] = result[length - 1]
            result.append(i)
            length += 1
        else: 
            pos = lower_bound(a, result, length, a[i])
            path[i] = result[pos - 1]
            result[pos] = i 
    return length
    

if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        result = []
        path = []
        last = -1

        n, p, q         =   map(int, input().split())
        prince_moves    =   list(map(int, input().split()))
        princess_moves   =   list(map(int, input().split()))
         
        pos = [0 for x in range(n**2 + 1)]
        for index in range(len(prince_moves)): 
            pos[prince_moves[index]] = index
        
        index_in_a = [0 for x in range(n**2 + 1)]
        
        for index in range(len(princess_moves)): 
            index_in_a[index] = pos[princess_moves[index]]
        
        res = LIS_binary_search(index_in_a)
        
        print("Case {}: {}".format(i + 1, res))

