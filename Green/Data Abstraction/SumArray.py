class sum_array:
    def __init__(self, a=0, b=1, c=2):
        self.x = a
        self.y = b
        self.i = c

    def __str__(self):
        s = "{0} {1}".format(self.x, self.y, self.i)
        return s


m,n = map(int, input().split())
k = int(input())
count = 0
arr = []

for i in range(k):
    x, y, value = map(int, input().split())
    p1 = sum_array(x, y, value)

    if p1.i > 0:
        count += 1
        arr.append(p1)

print(count)
for i in arr:
    print(i)




