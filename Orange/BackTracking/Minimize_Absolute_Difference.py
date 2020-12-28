def permutation(c, a, b, j, min_value, ans):
    """
    Create permutation to find combination of 4 out 5 elements 
    """
    global min_value_check 
    for i in range(5):
        if (b[i]):
            a[j] = i
            b[i] = False
            if j == 4:
                temp_check = check(a, c)[0]
                if temp_check < min_value_check: 
                    result_arr.append(check(a, c))
                    min_value_check = temp_check
            else:
                permutation(c, a, b, j + 1, min_value, ans)
            b[i] = True

def check(arr, origin_arr): 
    """
    Compute and check if the result is loweest
    @arr: the list of checked items
    
    Return: the index of items in with the lowest result
    """
    xa, xb, xc, xd = origin_arr[arr[0]], origin_arr[arr[1]], origin_arr[arr[2]], origin_arr[arr[3]]
    temp = abs((xa*xd - xb*xc)/(xb*xd))

    return temp, arr[0], arr[1], arr[2], arr[3]


if __name__ == "__main__":
    a, b, ans, minn = [], [], [], []
    c = list(map(int, input().split()))
    minn.append(1000000)
    minn.append(1)
    min_value_check = 10e9
    result_arr = []
    arr_min_value_check = []

    for i in range(5):
        a.append(i)

    for i in range(4):
        ans.append(0)

    b = [True] * 6
    permutation(c, a, b, 0, minn, ans)
    result = sorted(result_arr, key=lambda x:x[0]) 

    result = result[0][1:]
    print(*result)