from collections import Counter
BASE = 41
MOD = int(1e9 + 7)
MAXN = int(1e7)
mul = [1] * MAXN
hashS = [0] * MAXN

for i in range(1, MAXN): 
    mul[i] = (mul[i-1] * BASE) % MOD

def polyHash(keys):
    global hashS
    hashValue = 0
    n = len(keys)
    for i in range(n):
        hashValue = (ord(keys[i]) + (BASE * hashValue) % MOD) % MOD
        hashS[i + 1] = hashValue

    
def getHash(l, r):
    res = (hashS[r] - (hashS[l - 1] * mul[r - l + 1]) %MOD + MOD) % MOD
    return res


def process_letter(s, r0, r1): 
    res = ''
    for char in s: 
        if char == '0': 
           res += r0
        elif char == '1': 
            res += r1
    return res 

def process_r1(s, r0): 
    res = ''
    for char in s: 
        if char == '0': 
            res += r0
        else: 
            res += '1'
    


if __name__ == '__main__': 
    s = input()
    t = input()
    t_hash = polyHash(t)
    
    temp = Counter(s)
    zeros = temp['0']
    ones = temp['1']
    length = len(t)
    
    count_result = 0
    
    for i in range(len(t)):        
        chosen = [False, False]
        r = ['', '']
        length_arr = [0, 0]
        
        length_r0_all = (i+1) * zeros 
        check_r1 = (length - length_r0_all) % ones 
        
        
        if check_r1 == 0:
            length_arr[0] = i + 1
            length_arr[1] = (length - length_r0_all) // ones
        
            curr_index = 0
            Flag = True

            if length_arr[1] > 0:
                for char in s: 
                    curC = ord(char) - ord('0')
                    int_char = int(char)
                    if chosen[int_char] == False: 
                        r[curC] = getHash(curr_index + 1, curr_index + length_arr[curC]) 
                        chosen[int_char] = True
                    # print(getHash(curr_index + 1, curr_index + length_arr[curC] -1 + 1), r[curC])
                    # print(curr_index, curr_index + length_arr[curC] - 1 + 1)
                    if (getHash(curr_index + 1, curr_index + length_arr[curC] -1 + 1) != r[curC]):
                        Flag = False
                        break
                    if (r[0] == r[1]): 
                        Flag = False
                        break
                    curr_index = curr_index + length_arr[curC]
    
                
                if Flag: 
                    count_result += 1
    
    print(count_result)
        
        
         
        