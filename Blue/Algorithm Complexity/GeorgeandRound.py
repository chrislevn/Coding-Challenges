n, m = map(int, input().split())

arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

bestPossible = n

if bestPossible > m: 
  bestPossible = m

i = bestPossible
while i >= 0: 
  flag = True
  for j in range(i): 
    if (arr_n[j] > arr_m[m - i + j]):
       flag = False

  if flag: 
    print(n - i)
    exit()
    
  i -= 1