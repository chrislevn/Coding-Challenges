if __name__ == '__main__': 
    input_letter = input()
    # reverse_letter = input_letter[::-1]
    length = len(input_letter)

    is_panlindrome = [[False for i in range(length + 3)] for i in range(length+3)]
    
    for i in range(length): 
        is_panlindrome[i][i] = True 
    for i in range(length- 1, -1, -1): 
        for j in range(i + 1, length): 
            if (input_letter[i] == input_letter[j] and (i + 1 == j or is_panlindrome[i+1][j-1])): 
                is_panlindrome[i][j] = True
    
    degree_panlindrome = [[0 for i in range(length + 3)] for i in range(length + 3)]
    res = [0] * (length + 1)
    
    for i in range(length): 
        for j in range(i, length): 
            if (i == j): 
                degree_panlindrome[i][j] = 1
            elif is_panlindrome[i][j]: 
                mid = (i + j - 1) // 2
                degree_panlindrome[i][j] = degree_panlindrome[i][mid] + 1
            res[degree_panlindrome[i][j]] += 1
            
            
    for i in range(length - 2, 0, -1): 
        res[i] += res[i + 1]
            
    print(*res[1::])
    
        