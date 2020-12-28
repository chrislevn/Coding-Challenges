
t = int(input())

for i in range(t): 
    n = int(input())
    arr = list(map(int, input().split()))

    freq_arr = []
    for j in range(1, len(arr)+1): 
        freq_arr.append(j*(len(arr) - j + 1))

    res = 0
    for j in range(len(arr)): 
        if freq_arr[j] % 2!= 0: 
            res ^= arr[j]

    print(res)