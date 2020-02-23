n = int(input())
m = n
arr = []
count = 0

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)


def check_row(array, n, row, col):
    for d in range(n):
        if array[row][d] > array[row][col]:
            return False
    return True


def check_column(array, n, row, col):
    for e in range(n):
        if array[e][col] > array[row][col]:
            return False
    return True


def check_incline(array, n, row, col):
    for i in range(max(-row, -col), min(n - 1 - row, n - 1 - col) + 1):
        if array[row + i][col + i] > array[row][col]:
            return False
    return True


def check_reverse(array, n, row, col):
    for i in range(max(-row, -n + col + 1), min(n - 1 - row, col) + 1):
        if array[row + i][col - i] > array[row][col]:
            return False
    return True


def isChecked(array, n, row, col):
    if check_row(array, n, row, col) and check_column(array, n, row, col) and check_incline(array, n, row, col) and check_reverse(array, n, row, col):
        return True
    return False


for x in range(m):
    for y in range(n):
        if isChecked(arr, n, x, y):
            count += 1

print(count)
