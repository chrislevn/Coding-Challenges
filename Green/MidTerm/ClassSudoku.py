def checkCol():
    col = [[0] * 10 for i in range(10)]
    for j in range(9):
        for i in range(9):
            col[j][a[i][j]] += 1
            if col[j][a[i][j]] > 1:
                return False
    return True


def checkRow():
    row = [[0] * 10 for i in range(10)]
    for i in range(9):
        for j in range(9):
            row[i][a[i][j]] += 1
            if row[j][a[i][j]] > 1:
                return False
    return True

# Copy this
def checkSquareIndex(index):
    row = (index // 3) * 3
    col = index % 3 * 3
    Appear = [0] * 10
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            Appear[a[i][j]] += 1
            if (Appear[a[i][j]] > 1):
                return False
    return True


def checkSquare():
    for i in range(9):
        if checkSquareIndex(i) == False:
            return False
    return True


a = [list(map(int, input().split())) for i in range(9)]

if checkCol() and checkRow() and checkSquare():
    print("YES")
else:
    print("NO")
