visited = [[False for i in range(10)] for j in range(10)]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def is_valid(x, y, r, c):
    if (x >= 0) and (x < r) and (y >= 0) and (y < c):
        return board[x][y]
    return False

def DFS(x, y, count): 
    global max_step
    max_step = max(max_step, count)

    visited[x][y] = True

    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if is_valid(next_x, next_y, 10, 10) and not visited[next_x][next_y]: 
            
            DFS(next_x, next_y, count+1)

    visited[x][y] = False

if __name__ == "__main__":
    arr = list(map(int, input().split(' ')))
    n = arr[0]
    case = 1

    while n != 0: 
        board = [[False for i in range(10)] for j in range(10)]
        arr.pop(0)

        source_x = 0
        source_y = arr[0]
        max_step, sum_squares = 1, 0
    
        for i in range(n):
            skip, num_squares = arr.pop(0), arr.pop(0)
            sum_squares += num_squares
            board[i][skip:skip+num_squares] = [True] * num_squares
            
        DFS(source_x,source_y,1)
        result = sum_squares - max_step
        if result == 1:
            print("Case {}: {} square cannot be reached".format(case, result))
        else: 
            print("Case {}: {} squares cannot be reached".format(case, result))

        case += 1
        arr = list(map(int, input().split(' ')))
        n = arr[0]