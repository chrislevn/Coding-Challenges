n = int(input())
adja_list = []
count = 0
new_arr = []

for i in range(n): 
    arr = list(map(int, input().split()))
    adja_list.append(arr)

for i in range(len(adja_list)):
    count = 0
    for j in range(len(adja_list[i])):
        if adja_list[i][j] == 1:
            count += 1
    new_arr.append(count)

flag = False
for i in new_arr: 
    if i % 2 == 0:
        flag = True
    if i % 2 != 0: 
        flag = False
        print("NO")
        break

if flag == True: 
    print("YES") 
         

