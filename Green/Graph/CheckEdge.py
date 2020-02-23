n, x = map(int, input().split())
adja_list = []
count = 0

for i in range(n): 
    arr = list(map(int, input().split()))
    adja_list.append(arr)

for j in range(len(adja_list[x])): 
  if adja_list[x][j] == 1: 
      count += 1
      
print(count)