import math

n = int(input())

for i in range(n):
    x = int(input())
    square = math.ceil(x**0.5)
    row = col = square

    if square**2 - x < square:
        col = square**2 - x + 1
    else:
        row = x - (square - 1)**2

    if square % 2 == 1:
        row, col = col, row
    print("Case " + str(i+1) + ": " + str(abs(row)) + " " + str(abs(col)))