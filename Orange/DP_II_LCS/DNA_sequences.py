# LCS Top-down
MAXM, MAXN = 1005, 1005

def lcs_bottom_up(s1, s2, m, n, K): 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
                continue
            else: 
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

            for segment_length in range(1, min(i,j)+1): 
                if s1[i - segment_length] == s2[j - segment_length] and segment_length >= K: 
                    L[i][j] = L[i - segment_length][j - segment_length] + segment_length
                elif s1[i - segment_length] != s2[j - segment_length]: 
                    break
    return L[m][n]


if __name__ == '__main__': 
    K = int(input())
    while K != 0: 
        L = [[-1] * (MAXN + 1) for i in range(MAXM + 1)]
        first = input() 
        second = input()
        print(lcs_bottom_up(first, second, len(first), len(second), K))
        
        K = int(input())
        