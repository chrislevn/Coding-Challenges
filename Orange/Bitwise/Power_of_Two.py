def check(item): 
    if item & (item - 1) == 0: 
        return True 
    return False

def getBit(num, index): 
    return (num >> index) & 1


t = int(input())

for i in range(t): 
    n = int(input())
    arr = list(map(int, input().split()))

    flag = False
    
    for l in range(30): 
        sum_and = 0xFFFFFFFF
        for k in range(len(arr)): 
            if getBit(arr[k], l) == 1: 
                sum_and &= arr[k]
        if check(sum_and): 
            flag = True

    print("YES" if flag else "NO")
                

