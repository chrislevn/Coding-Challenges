def getHash(l, r):
    return (hashT[r] - hashT[l - 1] * power[r - l + 1] % MOD + MOD)  % MOD


s = input()
t = input()
BASE = 41
MOD = int(1e9 + 7)
count = [0] * 2
#số lượng số  0/1
for i in s:
    if (i == '0'): count[0] += 1
    else: count[1] += 1
#init Hash
m = len(t)
power = [1] * (m + 1)
hashT = [1] * (m + 1)
for i in range(1, m + 1):
    power[i] = (power[i - 1] * BASE) % MOD

ans = 0
for i in range(1, m + 1):
    hashT[i] = ( hashT[i - 1] * BASE + ord(t[i - 1]) ) % MOD

#lenZeros: chọn độ dài của R0
res = 0
length = [0] * 2
for lenZeros in range(1, len(t) + 1):
    if (count[0] * lenZeros >= m):
        break
    if (m - lenZeros * count[0]) % count[1] != 0:
        lenZeros += 1
        continue
    length[0] = lenZeros
    length[1] = (m - lenZeros * count[0]) // count[1]

    curIndex = 0 #1-base
    Chosen = [False] * 2
    R = [''] * 2
    Flag = True
    for i in range(len(s)):
        curC = ord(s[i]) - ord('0')
        if not Chosen[curC]:
            #R[curC] = t[curIndex:curIndex + length[curC]]
            R[curC] = getHash(curIndex + 1, curIndex + length[curC] - 1 + 1)
            Chosen[curC] = True
        if (getHash(curIndex + 1, curIndex + length[curC] -1 + 1) != R[curC]):
            Flag = False
            break
        if (R[0] == R[1]): 
            Flag = False
            break
        curIndex = curIndex + length[curC]
        
    print(R)
    if Flag:
        res += 1
        #print(R)
        #print(length)
        

print(res)
        
         


        

