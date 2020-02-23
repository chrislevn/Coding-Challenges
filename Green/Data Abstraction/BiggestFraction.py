class fraction:
    def __init__(self, a = 0, b = 1):
        self.tu = a
        self.mau = b

    def compare(self, other):
        return (self.tu * other.mau) - (self.mau * other.tu)

    def gcd(self):
        divisor = 0
        a = self.tu
        b = self.mau

        while b != 0:
            divisor = a % b
            a = b
            b = divisor
        return a

    def reduce(self):
        c = p1.gcd()

        self.tu //= c
        self.mau //= c
        return self

    def __str__(self):
        s = "{0} {1}".format(self.tu, self.mau)
        return s

n = int(input())
tu_arr = []
mau_arr = []

x, y = map(int, input().split())
p1 = fraction(x, y)

for i in range(1, n):
    x, y = map(int, input().split())
    p2 = fraction(x, y)

    if p1.compare(p2) < 0:
        p1 = p2

print(p1.reduce())



