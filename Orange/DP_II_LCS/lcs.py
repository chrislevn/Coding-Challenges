"""
Name: 
Christopher Le
Alvaro Martin Grande
"""

MAXM, MAXN = 100, 100
L = [[-1] * (MAXN + 1) for i in range(MAXM + 1)]


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

s1 = "abcabcabc"
s2 = "cbabcabc"
print(lcs_bottom_up(s1, s2, len(s1), len(s2)))