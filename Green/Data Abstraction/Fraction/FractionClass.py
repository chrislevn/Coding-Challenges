class Fraction:
    def __init__(self, a=0, b=1):
        self.nu = a
        self.de = b

    def sumFraction(self, p2):
        p3 = Fraction()

        p3.nu = self.nu * p2.de + self.de * p2.nu
        p3.de = self.de * p2.de
        p3.reduceFraction()
        return p3

    def reduceFraction(self):
        if (self.nu == 0):
            self.de = 1
            return
        x = self.gcd(abs(self.nu), abs(self.de))
        self.nu = self.nu // x
        self.de = self.de // x
        return

    def gcd(self, a, b):
        r = 0

        while (b != 0):
            r = a % b
            a = b
            b = r
        return a

    def __str__(self):
        s = "{0} {1}".format(self.nu, self.de)
        return s

x, y = map(int, input().split())
p1 = Fraction(x, y)
x, y = map(int, input().split())
p2 = Fraction(x, y)
p3 = p1.sumFraction(p2)
print(p3)