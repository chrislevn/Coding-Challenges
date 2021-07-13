# LCS Bottom-Up 
MAXM, MAXN = 125, 125
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

def LCS_ancestor(s1, s2, m, n): 
    length_LCS_ancestor = m + n -L[m][n]
    result = [""] * length_LCS_ancestor
    i = m
    j = n 
        
    while i > 0 and j > 0: 
        if s1[i - 1] == s2[j - 1]: 
            result[length_LCS_ancestor - 1] = s1[i - 1]
            i -= 1 
            j -= 1
            length_LCS_ancestor -= 1
        elif L[i-1][j] > L[i][j -1]: 
            result[length_LCS_ancestor - 1] = s1[i - 1]
            length_LCS_ancestor -= 1
            i -= 1
        else: 
            result[length_LCS_ancestor - 1] = s2[j - 1]
            length_LCS_ancestor -= 1
            j -= 1
            
    while i > 0: 
        result[length_LCS_ancestor - 1] = s1[i - 1]
        i -= 1 
        length_LCS_ancestor -= 1
        
    while j > 0:
        result[length_LCS_ancestor - 1] = s2[j - 1]
        j -= 1
        length_LCS_ancestor -= 1
            
    return ''.join(result)


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        s1 = input()
        s2 = input()
        
        lcs_bottom_up(s1, s2, len(s1), len(s2))
        lcs_ancestor_value = len(LCS_ancestor(s1, s2, len(s1), len(s2)))
        
        print("Case {}: {} {}".format(i + 1, lcs_ancestor_value, 0))
        
        
        