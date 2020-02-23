class FurthestPoint:
    def __init__(self, a=0, b=1):
        self.x = a
        self.y = b

    def findDistance(self, p2):
        distance = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        return distance

    def __str__(self):
        s = "{0} {1}".format(self.x, self.y)
        return s


Mx, My = map(int, input().split())
p1 = FurthestPoint(Mx, My)
arr = []
new_arr = []

n = int(input())
for i in range(n):
    Nx, Ny = map(int, input().split())
    p2 = FurthestPoint(Nx, Ny)

    new_arr.append(p2)

    sum_arr = p1.findDistance(p2)
    arr.append(sum_arr)

max_index = arr.index(max(arr))
print(new_arr[max_index])
