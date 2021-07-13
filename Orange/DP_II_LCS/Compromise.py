# LCS Top-down
MAXM, MAXN = 100, 100
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
    
    
def print_LCS(s1, s2, m, n): 
    length_LCS = L[m - 1][n - 1]
    result = [None] * length_LCS
    i = m - 1
    j = n - 1
    
    while i >= 0 and j >= 0: 
        if s1[i] == s2[j]: 
            result[length_LCS - 1] = s1[i]
            i -= 1 
            j -= 1
            length_LCS -= 1
        elif L[i-1][j] > L[i][j -1]: 
            i -= 1
        else: 
            j -= 1
    print(' '.join(result))
        
        
if __name__ == '__main__': 
    count_case = 1
    
    first_arr = []
    second_arr = []
    
    while True: 
        try: 
            input_letter = list(map(str, input().split()))
            if count_case % 2 != 0: 
                first_arr.extend(input_letter)

            else: 
                second_arr.extend(input_letter)
                
            if len(input_letter) == 0: 
                break

            if input_letter[0] == '#':
                if count_case % 2 != 0: 
                    first_arr.pop()
                else: 
                    second_arr.pop()
                    
                count_case += 1
                
                if count_case % 2 != 0: 
                    lcs_top_down(first_arr, second_arr, \
                                len(first_arr), \
                                len(second_arr))
                    
                    print_LCS(first_arr, second_arr, \
                                            len(first_arr), \
                                            len(second_arr))
                    
                    first_arr = []
                    second_arr = []
                    count_case = 1


        except EOFError: 
            break 
