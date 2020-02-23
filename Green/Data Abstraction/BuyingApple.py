class Apple:
    def __init__(self, a=0, b=1):
        self.weight = a
        self.price = b

    def compare(self, other):
        # init_wei = self.weight
        # init_pri = self.price

        if self.weight > other.weight:
            return True

        if self.weight == other.weight:
            if self.price > other.price:
                return True
            else:
                self.price = other.price
                self.weight = other.weight

                return False
        else:
            self.weight = other.weight
            self.price = other.price

            return False

    def __str__(self):
        s = "{0} {1}".format(self.weight, self.price)
        return s


n = int(input())
x, y = map(int, input().split())
p1 = Apple(x,y)
count = 0

for i in range(1, n):
    x, y = map(int, input().split())
    p2 = Apple(x, y)

    if p1.compare(p2) == False:
        count = i

print(count)

