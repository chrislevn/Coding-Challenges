road_arr = []

for i in range(4): 
    arr = list(map(int, input().split()))
    road_arr.append(arr)


for i in range(len(road_arr)):
    
    if sum(road_arr[i]) > 1 and road_arr[i][-1] == 1:
        print("YES")
        exit()
            
    if road_arr[i][-1] == 1:
        if road_arr[(i + 2) % 4][1] == 1 or road_arr[(i - 1 + 4) % 4][2] == 1 or road_arr[(i + 1) % 4][0] == 1: 
            print("YES")
            exit()


print("NO")
    