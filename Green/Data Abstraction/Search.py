class StudentScore:
    def __init__(self, a=0, b=1, c=2):
        self.digit = a
        self.math = b
        self.lit = c

    def __str__(self):
        s = "{1} {2}".format(self.digit, self.math, self.lit)
        return s


n, q = map(int, input().split())
arr = []
student_arr = []

for i in range(n):
    a, b, c = map(float, input().split())
    p1 = StudentScore(a, b, c)
    student_arr.append(p1)


for j in range(q):
    x = int(input())
    arr.append(x)

for m in range(len(arr)):
    for d in range(len(student_arr)):
        if arr[m] == student_arr[d].digit:
            print(student_arr[d])

