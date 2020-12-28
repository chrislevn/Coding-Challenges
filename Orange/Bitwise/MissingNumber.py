def getMissingNum(arr, n): 
    xor_num = 1
    xor_arr = arr[0]

    for i in range(2, n+2): 
        xor_num ^= i

    for i in range(1, n): 
        xor_arr ^= arr[i]

    print(xor_num, xor_arr)
    
    return xor_num ^ xor_arr
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7, 8, 9]
    res = getMissingNum(arr, 8)

    print(res)
