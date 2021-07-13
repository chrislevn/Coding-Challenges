# LCS Top-down
MAXM, MAXN = 2000, 2000
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


def solve(arr): 
    first_check_list = arr[0]
    max_result = 0
    for second_check_list in arr[1:]: 
        global L
        L = [[-1] * (len(second_check_list) + 1) for i in range(len(first_check_list) + 1)]
    
        # print('test', first_check_list, ''.join(second_check_list))
        max_result = max(max_result, lcs_top_down(first_check_list, \
                                    second_check_list, \
                                    len(first_check_list), \
                                    len(second_check_list)))
        
    return max_result
if __name__ == '__main__': 
    d = int(input())
    count_zero = 0 
    case_arr = []
    
    while count_zero < d: 
        arr = list(map(int, input().split()))
        case_arr.append(arr)
        if arr[0] == 0: 
            print('{}'.format(solve(case_arr) - 1))
            case_arr = []
            count_zero += 1
        