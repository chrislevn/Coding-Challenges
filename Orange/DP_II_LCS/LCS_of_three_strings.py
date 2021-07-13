# LCS Bottom-Up 
MAXM, MAXN, MAXK = 100, 100, 100
L = [[[-1] * (MAXN + 1) for i in range(MAXM + 1)] for j in range(MAXK + 1)]

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


def lcs_bottom_up_three(s1, s2, s3, m, n, l): 
    for i in range(m + 1): 
        for j in range(n + 1): 
            for k in range(l + 1):
                if i == 0 or j == 0 or k == 0: 
                    L[i][j][k] = 0
                elif s1[i - 1] == s2[j - 1] and s1[i - 1] == s3[k - 1] and s2[j - 1] == s3[k - 1]: 
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else: 
                    L[i][j][k] = max(L[i - 1][j][k], L[i - 1][j - 1][k], L[i - 1][j][k - 1], \
                                    L[i][j - 1][k], L[i][j][k - 1], L[i][j - 1][k - 1], \
                                    L[i - 1][j - 1][k - 1])
    
    return L[m][n][l]


if __name__ == '__main__':
    t = int(input())
    for i in range(t): 
        n, m, k = map(int, input().split())
        x, y, z = map(str, input().split())
        
        result = lcs_bottom_up_three(x, y, z, len(x), len(y), len(z))
        
        print(result)
        
        