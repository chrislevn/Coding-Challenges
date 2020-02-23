base_arr = []
result_arr = []

class Node: 
  def __init__(self, a= 0, b = 1): 
    self.x = a
    self.y = b
  def __str__(self): 
    s = "{0} {1}".format(self.x, self.y)
    return s

w, l = map(int, input().split())
while w != 0 and l != 0: 
  n = int(input())
  base_x, base_y = 0,0
  result_x, result_y = 0, 0
  w -= 1
  l -= 1
  w, l = l, w
  print(w, l)

  for i in range(n): 
    input_value = input().split()
    x = input_value[0]
    y = int(input_value[1])

    if x == "u":
      base_y += y
      if abs(y) <= w:
        result_y += y
      # if abs(y) > l: 
      #   result_x += min(w, y)
    if x == "d":
      base_y -= y
      if abs(y) <= w:
        result_y -= y
      # if abs(y) > l: 
      #   result_x -= min(w, y)
    if x == "r":
      base_x += y
      if abs(y) <= l:
        result_x += y
      if abs(y) > l: 
        result_x += min(l, y)
    if x == "l":
      base_x -= y
      if abs(y) <= l:
        result_x -= y
      if abs(y) > l: 
        result_x -= min(l, y)

  base_arr.append(Node(base_x, base_y))
  result_arr.append(Node(result_x, result_y))
  
  w, l = map(int, input().split())

for i in range(0, len(base_arr)):
  print("Robot thinks", base_arr[i])
  print("Actually at", result_arr[i])
  print()