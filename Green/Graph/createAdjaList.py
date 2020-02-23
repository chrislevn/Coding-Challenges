class Edge: 
  def __init__(self, u = 0, v = 1): 
    self.start = u
    self.end = v
  
  def __str__(self): 
    s = "{0} {1}".format(self.start, self.end)
    return s

n = int(input())
adja_list = []
edge_list = []
count = 0
count_mul = 1

for i in range(n): 
  arr = list(map(int, input().split()))
  adja_list.append(arr)

for i in range(len(adja_list)):
  for j in range(len(adja_list[i])):
    if adja_list[i][j] == 1:
      edge_list.append(Edge(i, j))

print(len(edge_list))
for i in range(len(edge_list)): 
  print(edge_list[i])




