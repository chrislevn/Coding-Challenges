result = []
path = []
last = -1

def printLIS(a): 
    global last 
    b = []
    i = last 
    while i != -1: 
        b.append(a[i])
        i = path[i]
        
    for i in range(len(b) - 1, -1, -1): 
        print(b[i], end=' ')
        
        
def LIS(a): 
    global last, result, path
    length = 0 
    path = [-1] * len(a)
    result = [1] * len(a)
    
    for i in range(1, len(a)): 
        for j in range(i): 
            if a[i] > a[j] and result[i] < result[j] + 1: 
                result[i] = result[j] + 1
                path[i] = j
                
    for i in range(len(a)): 
        if length < result[i]: 
            last = i 
            length = result[i]
            
    return length

# SAMPLE 
a = [2, 5, 12, 3]
print(LIS(a))
printLIS(a)


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

