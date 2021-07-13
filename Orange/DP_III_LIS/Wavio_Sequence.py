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
    length = 1
    path = [-1] * len(a)
    result = []
    result.append(0)
    #LIS bắt đầu từ vị trí 0 đến vị trí thứ i
    LIS_from_left = [1]
    
    for i in range(1, len(a)): 
        if a[i] <= a[result[0]]: 
            result[0] = i 
            # truoc i khong the tim ra so nao nho hon i
            LIS_from_left.append(1)

        elif a[i] > a[result[length - 1]]: 
            path[i] = result[length - 1]
            result.append(i)
            length += 1
            LIS_from_left.append(length)
        else: 
            #vi tri dau tien >= a[i]
            # LIS_from_left.append(pos - 1 + 1)
            pos = lower_bound(a, result, length, a[i])
            LIS_from_left.append(pos + 1)
            path[i] = result[pos - 1]
            result[pos] = i 
    return LIS_from_left
        
if __name__ == '__main__': 
    while True: 
        try: 
            n = int(input())
            arr = list(map(int, input().split()))
            
            LIS_left = LIS_binary_search(arr)
            LIS_right = LIS_binary_search(arr[::-1])[::-1]
            
            res = 0
            for i in range(len(LIS_left)): 
                temp = min(LIS_left[i], LIS_right[i]) * 2 - 1
                res = max(temp, res)

            print(res)

            if n == '': 
                exit()
        except EOFError: 
            exit()