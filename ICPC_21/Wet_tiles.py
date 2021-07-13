class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

def is_valid(x, y, r, c): 
    return x in range(r) and y in range(c)


x, y, t, l, w = map(int, input().split())
for i in range(2*l): 
