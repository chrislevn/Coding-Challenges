if __name__ == "__main__": 
    t = int(input())

    for i in range(t): 
        n, k, s = map(int, input().split())
        initial  = k -1 
        total = n+1
        remain = k-s
        remain_to_boss = n - s + 1

        option_1 = initial + total
        option_2 = initial + remain + remain_to_boss

        print("Case #{}: {}".format(i+1, min(option_1, option_2)))