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
            if a[i] >= a[j] and result[i] < result[j] + 1: 
                result[i] = result[j] + 1
                path[i] = j
                
    for i in range(len(a)): 
        if length < result[i]: 
            last = i 
            length = result[i]
            
    return length


if __name__ == '__main__': 
    n = int(input())
    arr = []

    count_negative_one = 0
    order = 0
    while True: 
        if n == -1: 
            count_negative_one += 1
            if count_negative_one == 2: 
                break
            else: 
                order += 1 
            arr = arr[::-1]
            print('Test #{}: \n  maximum possible interceptions: {}'.format(order, LIS(arr)))
            arr = []
        else: 
            count_negative_one = 0 
            arr.append(n)
            
        n = int(input())
            
        