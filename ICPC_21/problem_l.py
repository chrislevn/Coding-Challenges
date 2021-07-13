def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[m][n] 
  

n, k = map(int, input().split())
arr = []
for i in range(n):
    letter = input()
    arr.append(letter)

result = 0
for i in range(len(arr)): 
    for j in range(i, len(arr)): 
        if i != j:
            result = max(result, lcs(arr[i], arr[j]))

print(result)