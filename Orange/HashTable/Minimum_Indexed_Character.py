def poly_hash(keys): 
    hash_value = 0
    a = 33
    for i in range(len(keys)): 
        hash_value = ord(keys[i]) + a * hash_value
    return hash_value & 0x7FFFFFFF

MOD = 10**9 + 7 
MAXN = 10**6 + 7 
BASE = 26 
mul = [0] * MAXN
hashS = [0] * MAXN


mul[0] = 1
for i in range(1, MAXN): 
    mul[i] = (mul[i-1] * BASE) % MOD
    
def getHash(l, r):
    res = (hashS[r] - (hashS[l - 1] * mul[r - l + 1]) %MOD + MOD) % MOD
    return res


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        patt    = input()
        string  = input()
        flag = False
        
        for first_index in range(len(patt)): 
            first_hash = poly_hash(patt[first_index])
            for second_index in range(len(string)):
                second_hash = poly_hash(string[second_index])
                
                if first_hash == second_hash: 
                    print(patt[first_index])
                    flag = True
                    break
                    
            if flag: 
                break
        if not flag:
            print('No character present')        
        