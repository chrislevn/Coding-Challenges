from itertools import permutations


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
        
        
def LIS_Triple(a): 
    global last, result, path
    length = 0 
    path = [-1] * len(a)
    result = [a[i][2] for i in range(len(a))]
    
    for i in range(1, len(a)): 
        for j in range(i): 
            if a[i][0] > a[j][0] and a[i][1] > a[j][1] and result[i] < result[j] + a[i][2]: 
                result[i] = result[j] + a[i][2]
                path[i] = j
                
    for i in range(len(a)): 
        if length < result[i]: 
            last = i 
            length = result[i]
            
    return max(result)


if __name__ == '__main__': 
    n = int(input())
    count = 1
    while n != 0: 
        arr = []
        for i in range(n): 
            temp_arr = list(map(int, input().split())) 
            temp = list(permutations(temp_arr))
            
            arr.extend(temp)
        arr = sorted(arr)
        
        print("Case {}: maximum height =  {}".format(count, LIS_Triple(arr)))
        count += 1
        n = int(input())