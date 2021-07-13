import sys 

def bin_one(num):
    s = bin(num)[2:]
    return set([(len(s) - i - 1) for i in range(len(s)) if s[i] == "1"])

if __name__ == "__main__": 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        max_bin_len = len(bin(max(arr))[2:])

        C = [0] * max_bin_len
        S = 0
        total_sum = 0
        for i in range(0, n):
            S ^= arr[i]
            index_ones = bin_one(S)
            for j in range(len(C)):
                if j in index_ones:
                    total_sum += (i + 1 - C[j]) * pow(2, j)
                    C[j] += 1
                else:
                    total_sum += C[j] * pow(2, j)

        print(total_sum)
