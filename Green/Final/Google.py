t = int(input())

for i in range(t): 
    n = int(input())
    arr = list(map(int, input().split()))
    
    length = len(arr) - 1
    index = 0 
    
    check_arr = []
    
    while index <= length: 
        if index+1 <= length: 
            remain = arr[index+1] - arr[index] 
            check_arr.append(remain)
            if remain != check_arr[-1]: 
                check_arr.append(remain)
                
    count = 1
    res = 0
    for j in range(1, len(check_arr)): 
        if check_arr[j] != check_arr[j-1]: 
            count = 1
        else: 
            count += 1
        res = max(res, count)
        
    print('Case #' + str(i+1) + ': '+ str(check_arr))