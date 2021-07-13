def r3gz3n(number):
    sum_of_elements = sum([int(digit) for digit in str(number)])
    return number ^ sum_of_elements

if __name__ == "__main__": 
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = 0
    s = dict()
    count = 0
    
    for number in arr: 
        process_number = r3gz3n(number)
        max_value = max(max_value, process_number)
        
        if process_number not in s: 
            s[process_number] = 1       
        else: 
            s[process_number] += 1
            count += 1
    
    temp_s = [x for x in s if s[x] > 1]
    
    if len(temp_s) > 0: 
        max_freq = max(s.values())
        min_value = min(x for x in s if s[x] == max_freq)
        print(min_value, count)
    else:
        print(max_value, count)
    