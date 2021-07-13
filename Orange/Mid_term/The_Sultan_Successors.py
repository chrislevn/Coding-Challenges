n = 8
board = [[0] * n for i in range(n)]

def print_solution(): 
    for i in range(n): 
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()

def calculate_sum(actual_board, temp_board): 
    sum_value = 0
    for i in range(n): 
        for j in range(n): 
            if temp_board[i][j] == 1: 
                sum_value += actual_board[i][j]
    return sum_value

def check(board, row, col): 
    for i in range(row): 
        if board[i][col]: 
            return False
    
    i = row
    j = col 

    while i >= 0 and j >= 0: 
        if board[i][j]: 
            return False
        
        i -= 1
        j -= 1
    
    i = row
    j = col 

    while j < n and i >= 0: 
        if board[i][j]: 
            return False
        i -= 1
        j += 1

    return True

def NQuen(board, row): 
    global final_result
    if row == n: 
        final_result = max(final_result, calculate_sum(actual_board, board))
    for j in range(n): 
        if check(board, row, j): 
            board[row][j] = 1
            NQuen(board, row + 1)
            board[row][j] = 0
    

if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        actual_board = []
        final_result = 0

        for j in range(8): 
            arr = list(map(int, input().split()))
            actual_board.append(arr)
        
        NQuen(board, 0)
        print(final_result)
 
