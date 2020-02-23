

x, y = map(int, input().split())
p1 = Fraction(x, y)
x, y = map(int, input().split())
p2 = Fraction(x, y)
p3 = p1.sumFraction(p2)
print(p3)


