n, t = map(int, input().split())
arr = list(map(int, input().split()))

r, l = 0, 0 

count_update = 0
max_count = 0


for r in range(n):
    
    while t < arr[r]: 
        t += arr[l]
        l += 1
        count_update -= 1
        if count_update > max_count: 
            max_count = count_update

    t -= arr[r]
    count_update += 1
    if count_update > max_count: 
            max_count = count_update

    #print("l", l, "r", r)
    #print("count", count_update)
print(max_count)


