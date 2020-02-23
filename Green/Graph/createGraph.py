class Edge:
    def __init__(self, u = 0, v = 1):
        self.i = u
        self.j = v

    def __str__(self):
        s = '{0} {1}'.format(self.i, self.j)
        return s


n = int(input())
adja_arr = []
edge_list = []
count = 0

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    adja_arr.append(arr)

for i in range(len(adja_arr)):
    for j in range(i + 1, len(adja_arr[i])):
        if adja_arr[i][j] == 1:
            count += 1
            edge_list.append(Edge(i, j))


print(count)
for value in edge_list:
    print(value.i, value.j)
