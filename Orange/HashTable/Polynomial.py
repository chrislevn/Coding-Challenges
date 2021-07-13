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


if __name__ == "__main__": 
    keys = "Anne"
    print(poly_hash(keys))
        