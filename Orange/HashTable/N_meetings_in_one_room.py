if __name__ == "__main__": 
    t = int(input())
    for i in range(t): 
        size        =   int(input())
        first_arr   =   list(map(int, input().split()))
        second_arr  =   list(map(int, input().split()))
        
        count = 0 # count the number of meetings
        result = []
        temp_meeting_arr = []
        
        for idx in range(len(first_arr)): 
            temp_meeting_arr.append((second_arr[idx], first_arr[idx], idx))
            
        temp_meeting_arr.sort()
        temp_idx = 0
        result.append(temp_meeting_arr[0][2] + 1)
        
        for idx in range(1, len(temp_meeting_arr)): 
            if temp_meeting_arr[idx][1] > temp_meeting_arr[temp_idx][0]: 
                result.append(temp_meeting_arr[idx][2] + 1)
                temp_idx = idx

        print(*result)
                
        
        
            