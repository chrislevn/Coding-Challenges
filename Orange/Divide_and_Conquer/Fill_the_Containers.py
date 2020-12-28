from sys import maxunicode


def checkTempFill(temp, arr, m): 
    temp_sum = 0
    check_arr = []
    total_check = []
    
    for i in range(len(arr)): 
        temp_sum += arr[i]

        if temp_sum <= temp: 
            check_arr.append(arr[i])
        else: 
            total_check.append(check_arr)
            check_arr = []
            check_arr.append(arr[i])
            temp_sum = arr[i]
            
    total_check.append(check_arr)
    return len(total_check) <= m


def binarySearch(a, left, total, m):
    right = total
    res = -1 
    while left <= right:
        mid = (left + right) // 2
        if checkTempFill(mid, a, m):
            res = mid
            right = mid - 1
        else: 
            left = mid + 1
    return res


if __name__ == "__main__":
    while True:
        try:  
            n, m = map(int, input().split())
            c = list(map(int, input().split()))

            min_value = max(c)
            max_value = sum(c)

            print(binarySearch(c, min_value, max_value, m))

        except EOFError: 
            break
        

