def trading_wine(arr): 
    temp = arr[0]
    res = abs(arr[0])

    for i in range(1, len(arr)): 
        temp += arr[i]
        res += abs(temp)

    return res

if __name__ == "__main__": 
    n = int(input())

    while n != 0: 
        arr = list(map(int, input().split()))
        n = int(input())

        print(trading_wine(arr))