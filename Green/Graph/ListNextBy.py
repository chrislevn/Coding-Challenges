class Edge:
    def __init__(self, u=0, v=1):
        self.start = u
        self.end = v

    def __str__(self):
        s = "{0} {1}".format(self.start, self.end)
        return s


m, k = map(int, input().split())
new_arr = []
value_arr = []
result_arr = []
index_arr = []

for i in range(m):
    u, v, w = map(int, input().split())
    value_arr.append(Edge(u, v))
    new_arr.append(w)

sort_arr = sorted(new_arr)

for i in range(k):
    index_num = sort_arr[i]
    index_value = new_arr.index(index_num)
    result_arr.append(value_arr[index_value])

result_arr.reverse()
for i in result_arr:
    print(i)
