n = int(input())
while n != 0: 
    binary = str(bin(n).replace('0b', ''))[::-1]
    a, b = ['0']*len(binary), ['0']*len(binary)

    count = 1
    for i in range(len(binary)): 
        if binary[i] == '1': 
            if count % 2 != 0: 
                a[i] = '1'
            else:
                b[i] = '1'
            count += 1
        
    a_text, b_text = ''.join(a)[::-1], ''.join(b)[::-1]
    print(int(a_text, 2), int(b_text, 2))

    n = int(input())


def solve():
    n = int(input())
    if n == 0:
        exit()
    a = b = 0
    flag = 1
    #bit 1 lẻ, bit 1 chẵn
    #dãy 32 bits
    for i in range(32):
        if (n >> i) & 1:
            if flag:
                a += 1 << i
            else:
                b += 1 << i
            #if (flag == lẻ) flag = chẵn
            #else flag = lẻ
            #flag ^= 1
    print(a, b)

while True:
    solve()
