import math


class point_triangle:
    def __init__(self, a=0, b=1):
        self.x = a
        self.y = b

    def findDistance(self, p2):
        distance = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        return distance

    def __str__(self):
        s = "{0} {1}".format(self.x, self.y)
        return s


n = int(input())
arr = []
point_arr = []
result = 0

for i in range(n):
    for j in range(3):
        x, y = map(int, input().split())
        p1 = point_triangle(x, y)
        point_arr.append(p1)

    a = math.sqrt((point_arr[0].x - point_arr[1].x)**2 + (point_arr[0].y - point_arr[1].y)**2)
    b = math.sqrt((point_arr[1].x - point_arr[2].x)**2 + (point_arr[1].y - point_arr[2].y)**2)
    c = math.sqrt((point_arr[2].x - point_arr[0].x)**2 + (point_arr[2].y - point_arr[0].y)**2)

    half_p = (a + b + c) / 2
    mul = half_p * (half_p - a) * (half_p - b) * (half_p - c)
    result = math.sqrt(mul)
    arr.append(result)
    point_arr.clear()


final = sum(arr)
final_result = "%.2f" % round(final, 2)

print(final_result)

