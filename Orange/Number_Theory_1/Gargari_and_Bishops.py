def is_valid(x, y): 
    return x in range(len(table)) and y in range(len(table[0]))

if __name__ == '__main__': 
    n = int(input())
    table = []
    constant_main = [0 for i in range(2*n)]
    constant_other = [0 for i in range(2*n)]

    dx = [-1, 1, 3]
    dy = [-1, 1, 3]

    for i in range(n): 
        arr = list(map(int, input().split()))
        table.append(arr)
    
    for row in range(len(table)): 
        for col in range(len(table[0])): 
            const_value_main = row + col
            const_value_other = row - col + n

            constant_main[const_value_main] += table[row][col]
            constant_other[const_value_other] += table[row][col]
    
    x = [0] * 2
    y = [0]* 2
    res = [-1] * 2

    for row in range(len(table)): 
        for col in range(len(table[0])): 
            temp = 0
            pos = (row + col) % 2
            temp += constant_main[row + col] + constant_other[row - col + n] - table[row][col]

            if res[pos] < temp: 
                res[pos] = temp
                x[pos] = row + 1
                y[pos] = col + 1

        
    print(res[0] + res[1])
    print(x[0], y[0], x[1], y[1])


        
