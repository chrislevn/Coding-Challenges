class Edge:
    def __init__(self, u = 0, v = 1):
        self.i = u
        self.j = v

    def __str__(self):
        s = "{0} {1}".format(self.i, self.j)
        return s


n = int(input())
adjacent_matrix = []

flag = True

for i in range(n):
    arr = list(map(int, input().split()))
    adjacent_matrix.append(arr)

for i in range(len(adjacent_matrix)):
    for j in range(i + 1, len(adjacent_matrix)):
        if adjacent_matrix[i][j] != adjacent_matrix[j][i]:
            flag = False

if flag:
    print("YES")
else:
    print("NO")


