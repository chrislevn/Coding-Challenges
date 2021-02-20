def changing_signs(arr, num_of_swap): 
    temp_sum = sum(arr)
    min_abs_value = 10e9

    
    for i in range(len(arr)):
        if abs(arr[i]) < min_abs_value: 
            min_abs_value = abs(arr[i]) 
        if arr[i] < 0 and num_of_swap > 0: 
            temp_sum += abs(arr[i]) * 2
            num_of_swap -= 1
        
    if num_of_swap > 0: 
        if num_of_swap % 2 != 0: 
            temp_sum -= 2 * min_abs_value 
    
    return temp_sum


if __name__ == "__main__": 
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(changing_signs(arr, k))
