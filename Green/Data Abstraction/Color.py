import collections as co


class Color:
    def __init__(self, color_id):
        self.id = color_id
        self.sum_length = 0
        self.count = 0

    def update_len(self, new_len):
        self.sum_length += new_len
        self.count += 1


n = int(input())
colors = []
code_arr = []

for i in range(1001):
    p1 = Color(i)
    colors.append(p1)

for i in range(n):
    x, y = map(int, input().split())
    colors[x].update_len(y)
    p2 = Color(x)
    code_arr.append(p2.id)

k = co.Counter(code_arr)
print(len(k))

for i in range(1, 1001):
    if colors[i].count > 0:
        print(i, colors[i].sum_length, colors[i].count)
