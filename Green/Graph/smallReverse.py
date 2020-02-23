class Edge: 
  def __init__(self, u = 0, v = 1): 
    self.start = u
    self.end = v
  
  def __str__(self): 
    s = "{0} {1}".format(self.start, self.end)
    return s

m , k = map(int, input().split())
new_arr =[]
value_arr = []
result_arr = []
index_arr = []

for i in range(m):
  u, v, w = map(int, input().split())
  value_arr.append(Edge(u, v))
  new_arr.append(w)

for i in range(k): 
  small = min(new_arr)
  index_num = new_arr.index(small) + i
  index_arr.append(index_num)
  new_arr.remove(small)

index_arr.reverse()
for i in index_arr: 
  print(value_arr[i])

