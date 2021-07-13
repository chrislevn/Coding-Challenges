if __name__ == "__main__": 
    n, m = map(int, input().split())
    boy = list(map(int, input().split()))
    girl = list(map(int, input().split()))

    RECURSION_LIMIT = n*m*2

    boy_arr = [0 for i in range(n)]
    girl_arr = [0 for i in range(m)]
    if boy[0] > 0: 
        for index in boy[1:]: 
            boy_arr[index] = 1
    if girl[0] > 0: 
        for index in girl[1:]: 
            girl_arr[index] = 1
    
    i = 0 
    check_sum_boy = sum(boy_arr)
    check_sum_girl = sum(girl_arr)

    while (check_sum_boy + check_sum_girl) < (n+m) and i < RECURSION_LIMIT: 
        boy_index = (i % n)
        girl_index = (i % m)

        if boy_arr[boy_index] or girl_arr[girl_index] == 1: 
            if boy_arr[boy_index] == 0:
                boy_arr[boy_index] = 1 
                check_sum_boy += 1
            if girl_arr[girl_index] == 0:
                girl_arr[girl_index] = 1
                check_sum_girl += 1

        i += 1
    
    print("YES" if (check_sum_boy + check_sum_girl) == (n+m) else "NO")
    