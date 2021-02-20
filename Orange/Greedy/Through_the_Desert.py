if __name__ == '__main__':
    input_statement = input().split(' ')
    
    total_consume = 0
    last_visited = 0
    leak = 0
    leak_count = 0
    curr_fuel_consumption = int(input_statement[-1])
    
    while input_statement[-1] != '0': 
     
            
        # last_visited = int(input_statement[0])
        curr_visited = int(input_statement[0])
        
        distance = curr_visited - last_visited
        total_consume += (curr_fuel_consumption / 100) * distance + leak_count*distance
        last_visited = curr_visited
    
        if input_statement[1] == "Fuel": 
            curr_fuel_consumption = int(input_statement[-1])
        elif input_statement[1] == "Leak": 
            leak_count += 1
        elif input_statement[-1] == "Mechanic": 
            leak_count = 0
        elif input_statement[1] == "Gas": 
            total_consume = 0
        
        if input_statement[-1] == 'Goal': 
            print('{:.3f}'.format(total_consume))
            
            total_consume = 0
            last_visited = 0
            leak = 0 
            leak_count = 0 
            
        input_statement = input().split(' ')