def check_accept(check, item_arr): 
    for item in item_arr:
        if check & item == 0: 
            return False
    return True


t = int(input())

for i in range(t): 
    n, k = map(int, input().split())

    res = 0
    temp_arr = []
    for j in range(n): 
        dish_input = input()
        temp_arr.append(int(dish_input, 2))

    check_arr = []

    for j in range(2**k):
        check_arr.append(j)
    
    # print(check_arr)

    res = []
    
    for j in range(k+1): 
        for check in check_arr: 
            if check_accept(check, temp_arr): 
                res.append(bin(check).count('1'))
    
    print(min(res))
    