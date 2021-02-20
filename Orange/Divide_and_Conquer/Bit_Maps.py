def count(arr, value): 
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])): 
            if arr[i][j] == value: 
                result += 1
    return result


def D2B(arr, x, y, row, col):
    result = ''

    new_arr = [line[y:y+col] for line in arr[x:x+row]]

    if count(new_arr, '0') == row*col: 
        result += '0'
        return result
    elif count(new_arr, '1') == row*col: 
        result += '1'
        return result
    elif col == 0 or row == 0: 
        return ''
    else: 
        result += 'D'

        result += D2B(arr, x, y, (row+1)//2, (col+1)//2)
        result += D2B(arr, x, (y+col+1)//2, (row+1)//2, col//2)
        result += D2B(arr, (x+row+1)//2, y, row//2, (col+1)//2)
        result += D2B(arr, (x+row+1)//2, (y+col+1)//2, row//2, col//2)

    return result

if __name__ == "__main__":
    line = input().split(' ')

    while line[0] != '#':
        type = line[0]
        row, col = int(line[1]), int(line[2])

        if type == 'B': 
            temp = list(input())
            arr = [temp[i:i + col] for i in range(0, col * row, col)]
            print(D2B(arr, 0, row, 0, col))

        elif type == 'D': 
            arr = list(input())
                    
        line = input().split(' ')



if __name__ == "__main__":
    line = input().split(' ')

    while line[0] != '#':
        type = line[0]
        row, col = int(line[1]), int(line[2]) 