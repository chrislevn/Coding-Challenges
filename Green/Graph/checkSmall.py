n = int(input())
adja_list = []
count = 0

for i in range(n): 
  u, v, w = map(int, input().split())
  adja_list.append(w)

min_num = min(adja_list)
for i in range(len(adja_list)): 
  if adja_list[i] == min_num: 
    count += adja_list[i]

print(count)


