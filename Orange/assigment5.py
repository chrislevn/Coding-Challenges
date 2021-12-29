set_list = [3, 34, 4, 12, 5, 2]
sum_value = 12

# test 5
set_list2 = [3, 34, 4, 12, 5, 2]
sum_value2 = 30

def solve(set_list, sum_value): 
    for i in range(len(set_list)-1): 
        remain = sum_value - set_list[i]
        for j in range(i+1, len(set_list)): 
            if remain == set_list[j]: 
                return True
    return False


# print(solve(set_list2, sum_value2))

def solve_dp(set_list, sum_value): 
    n = len(set_list)
    arr =([[False for i in range(sum_value + 1)] for i in range(n + 1)])
    
    for i in range(n + 1): 
        arr[i][0] = True
    
    for i in range(1, sum_value + 1): 
        arr[0][i] = False

    for i in range(1, n + 1): 
        for j in range(1, sum_value + 1): 
            if j < set_list[i-1]: 
                arr[i][j] = arr[i-1][j]
            else: 
                arr[i][j] = (arr[i-1][j] or arr[i-1][j-set_list[i-1]])
    return arr[n][sum_value]

print(solve_dp(set_list2, sum_value2))

# Returns true if there exists a subsequence of `A[0…n]` with the given sum
result = []

def subsetSum(A, n, k):
    sol = k
    current = A[n]
    

    if k == 0:
        return result
        return True
 
    if n < 0 or k < 0:
        return False
 
    remain = sol - current
    result.append((current, remain))
    
    include = subsetSum(A, n - 1, remain)
    exclude = subsetSum(A, n - 1, k)

    return include or exclude
 

setList = [3, 34, 4, 12, 5, 2]
sol = 9

print(subsetSum(setList, len(setList) - 1, sol))
