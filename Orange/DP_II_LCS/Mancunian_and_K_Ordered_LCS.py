import sys
sys.setrecursionlimit(100000)

MAX = 200

def lcs_recursion(n, m, k): 
    global dp, first, second
    if k < 0: 
        return -10**7

    if m <= 0 or n <= 0: 
        return 0 

    ans = dp[n][m][k]

    if ans != -1: 
        return ans

    ans = max(lcs_recursion(n-1, m, k), lcs_recursion(n, m-1, k))
    if first[n - 1] == second[m - 1]: 
        ans = max(ans, 1 + lcs_recursion(n-1, m-1, k))
    ans = max(ans, 1 + lcs_recursion(n-1, m-1, k-1))
    
    dp[n][m][k] = ans

    return ans


# def lcs_bottom_up(dp, s1, s2, m, n, K): 
#     for i in range(m + 1): 
#         for j in range(n + 1): 
#             if i == 0 or j == 0: 
#                 L[i][j] = 0
#                 continue
#             else: 
#                 L[i][j] = max(L[i - 1][j], L[i][j - 1])

#             for segment_length in range(1, min(i,j)+1): 
#                 if s1[i - segment_length] == s2[j - segment_length] and segment_length >= K: 
#                     L[i][j] = L[i - segment_length][j - segment_length] + segment_length
#                 elif s1[i - segment_length] != s2[j - segment_length]: 
#                     break
#     return L[m][n]

if __name__ == '__main__': 
    n, m, k = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    dp = [[[-1 for i in range(k+1)] for j in range(m+1)] for l in range(n+1)]

    print(lcs_recursion(n, m, k))

