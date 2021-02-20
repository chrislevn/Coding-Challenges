def findNumber(n, k): 
    arr = sorted([int(x) for x in str(n)])
    temp_arr = arr.copy()
    sum_of_arr = sum(arr)
    if sum_of_arr >= k: 
        return 0
    else: 
        remain = k - sum_of_arr 
        for i in range(len(arr)): 
            temp_arr[i] = arr[i] + remain
            if temp_arr[i] > 9: 
                temp_arr[i] = 9
                remain -= (9 - arr[i])
            else: 
                remain -= remain

    res = 0
    # print(arr)
    for i in range(len(arr)): 
        if arr[i] != temp_arr[i]: 
            res += 1

    return res

if __name__ == "__main__": 
    k = int(input())
    n = int(input())

    print(findNumber(n, k))