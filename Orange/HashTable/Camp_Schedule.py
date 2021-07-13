from collections import Counter
from sys import prefix

MOD = 10**9 + 7 
MAXN = 10**6 + 7 
BASE = 26 
mul = [0] * MAXN
hashS = [0] * MAXN

mul[0] = 1
for i in range(1, MAXN): 
    mul[i] = (mul[i-1] * BASE) % MOD

def poly_hash(keys): 
    hashValue = 0
    n = len(keys)
    for i in range(n):
        hashValue = (ord(keys[i]) - 97 + (BASE * hashValue) % MOD) % MOD
        hashS[i + 1] = hashValue

def getHash(l, r):
    res = (hashS[r] - (hashS[l - 1] * mul[r - l + 1]) %MOD + MOD) % MOD
    return res


if __name__ == "__main__": 
    s = input()
    t = input()
    
    st = ''
    count_s = Counter(s)
    count_t = Counter(t)
    
    if count_s['0'] < count_t['0'] or count_s['1'] < count_t['1']: 
        print(s)
        exit()
        
    count_s['0'] -= count_t['0']
    count_s['1'] -= count_t['1']
    count_t['1'] = 0
    count_t['0'] = 0
    
    poly_hash(t)
    MaxPrefixDuplicate = 0
    length_t = len(t)
    
    for len in range(length_t - 1, -1, -1):
        if getHash(1, len) == getHash(length_t - len + 1, length_t):
            MaxPrefixDuplicate = len
            break 
    
    for i in range(MaxPrefixDuplicate, length_t):
        if t[i] == '0': 
            count_t['0'] += 1
        else: 
            count_t['1'] += 1
        st += t[i]
    
    mNeed = length_t - MaxPrefixDuplicate
    res = t
    
    while (count_s['0'] >= count_t['0'] and count_s['1'] >= count_t['1']): 
        count_s['0'] -= count_t['0']
        count_s['1'] -= count_t['1']
        
        for i in range(mNeed): 
            res += st[i]
    
    for i in range(count_s['0']): 
        res += '0'
    for i in range(count_s['1']): 
        res  += '1'       
    print(res)
    
    