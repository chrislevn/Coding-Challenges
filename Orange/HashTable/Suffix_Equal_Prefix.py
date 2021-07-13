MOD = 10**9 + 7 
MAXN = 10**6 + 7 
BASE = 26 
mul = [0] * MAXN
hashS = [0] * MAXN

def polyHash(keys):
    hashValue = 0
    n = len(keys)
    for i in range(n):
        hashValue = (ord(keys[i]) - 97 + (BASE * hashValue) % MOD) % MOD
        hashS[i + 1] = hashValue

def getHash(l, r):
    res = (hashS[r] - (hashS[l - 1] * mul[r - l + 1]) %MOD + MOD) % MOD
    return res

def count_suffix(input_letter): 
    start = 1
    length = len(input_letter)
    count = 0
    while start < length: 
        suffix = getHash(length - start + 1,n)
        preffix = getHash(1, start)
                
        if preffix == suffix: 
            count += 1
        start += 1
    return count


mul[0] = 1
for i in range(1, MAXN): 
    mul[i] = (mul[i-1] * BASE) % MOD


if __name__ == "__main__": 
    t = int(input())
    for i in range(t): 
        letter = input()
        hashS[0] = 0
        n = len(letter)
        polyHash(letter)

        print("Case {}: {}".format(i+1, count_suffix(letter)))
    