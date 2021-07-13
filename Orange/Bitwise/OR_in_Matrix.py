def sum_or(arr, i, j, m, n):
    res = 0
    for idx in range(m): 
        res |= arr[idx][j]
    for idx in range(n): 
        res |= arr[i][idx]
    return res

def check(B_arr, A_arr): 
    m = len(B_arr)
    n = len(B_arr[0])
    
    for i in range(m): 
        for j in range(n): 
            if B_arr[i][j] != sum_or(A_arr, i, j, m, n): 
                return False
    return True

def print_table(arr): 
    for i in range(len(arr)): 
        print(*arr[i])

if __name__ == '__main__': 
    m, n = map(int, input().split()) 
    B_arr = [] 
    A_arr = [[1 for x in range(n)] for y in range(m)]
    for i in range(m): 
        temp = list(map(int, input().split()))
        B_arr.append(temp)
    for i in range(len(B_arr)): 
        for j in range(len(B_arr[0])): 
            if B_arr[i][j] == 0: 
                for idx in range(m): 
                    A_arr[idx][j] = 0
                for idx in range(n): 
                    A_arr[i][idx] = 0

    if check(B_arr, A_arr): 
        print("YES")
        print_table(A_arr)
    else: 
        print("NO")