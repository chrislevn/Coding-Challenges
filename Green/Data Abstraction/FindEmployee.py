class Employee:
    def __init__(self, a=0, b=1, c=2):
        self.code = a
        self.name = b
        self.year = c

    def __str__(self):
        s = "{0} {1} {2}".format(self.code, self.name, self.year)
        return s


n = int(input())
arr = []
code_arr = []
year_arr = []
new_arr = []
new_code_arr = []

for i in range(n):
    x, y,  = input().split()
    p1 = Employee(x, y, )
    arr.append(p1)
    code_arr.append(int(p1.code))
    year_arr.append(int(p1.year))

for i in range(len(arr)):
    if int(arr[i].year) == int(min(year_arr)):
        new_arr.append(arr[i])
        new_code_arr.append(arr[i].code)

for i in range(len(new_arr)):
    if int(new_arr[i].code) == int(min(new_code_arr)):
        print(new_arr[i])

