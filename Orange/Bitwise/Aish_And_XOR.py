n = int(input())
num = list(map(int, input().split(" ")))
xor_sum = [0, num[0]]

temp_xor = num[0]
for i in range(1, len(num)):
    temp_xor ^= num[i] 
    xor_sum.append(temp_xor)

temp_zero = 0 if num[0] != 0 else 1
zero_arr = [0, temp_zero]
for i in range(1, len(num)): 
    if num[i] == 0: 
        temp_zero += 1
    zero_arr.append(temp_zero)


q = int(input())
for i in range(q): 
    l, r = map(int, input().split())    

    xor_res = xor_sum[r] ^ xor_sum[l-1]
    zero_res = zero_arr[r] - zero_arr[l-1]

    print(xor_res, zero_res)

