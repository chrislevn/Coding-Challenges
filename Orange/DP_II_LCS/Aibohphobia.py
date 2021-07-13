import sys 
sys.setrecursionlimit(6200)

# LCS Top-down
MAXM, MAXN = 6200, 6200
L = [[-1] * (MAXN + 1) for i in range(MAXM + 1)]

def lcs_top_down(s1, s2, m, n): 
    if m == 0 or n == 0: 
        return 0
    if L[m - 1][n - 1] != -1: 
        return L[m - 1][n - 1] 
    if s1[m - 1] == s2[n - 1]: 
        L[m - 1][n - 1] = 1 + lcs_top_down(s1, s2, m - 1, n - 1)
        return L[m - 1][n - 1]
    else: 
        L[m - 1][n - 1] = max(lcs_top_down(s1, s2, m, n - 1), lcs_top_down(s1, s2, m - 1, n))
        return L[m - 1][n - 1]

def lcs_bottom_up(s1, s2, m, n): 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
            else: 
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                
    return L[m][n]
    
    
def print_LCS(s1, s2, m, n): 
    length_LCS = L[m][n]
    result = [""] * length_LCS
    i = m
    j = n 
    
    while i > 0 and j > 0: 
        if s1[i - 1] == s2[j - 1]: 
            result[length_LCS - 1] = s1[i - 1]
            i -= 1 
            j -= 1
            length_LCS -= 1
        elif L[i-1][j] > L[i][j -1]: 
            i -= 1
        else: 
            j -= 1
    print(''.join(result))


if __name__ == '__main__': 
    while True: 
        try: 
            input_letter = input()
            reverse_letter = input_letter[::-1]
            
            temp_lcs_value = lcs_bottom_up(input_letter, reverse_letter, \
                        len(input_letter), len(reverse_letter))
            
            print(len(input_letter) - temp_lcs_value)
            
            # print_LCS(input_letter, reverse_letter, \
            #             len(input_letter), len(reverse_letter))
            
            if input_letter == '': 
                break
        except EOFError: 
            break 

