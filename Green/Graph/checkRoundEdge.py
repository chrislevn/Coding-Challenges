n = int(input())
adja_list = []
count = 0
count_mul = 1

for i in range(n): 
  u, v, w = map(int, input().split())
  if u == v:
    count += 1
    count_mul = count_mul * w 
    
count_mul = count_mul % (10^6 + 7)

print(count, count_mul)


