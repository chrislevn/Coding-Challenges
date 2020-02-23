class Time:
    def __init__(self, date = 0, month = 0, year = 0):
        self.day = date
        self.month = month
        self.year = year

    def check_last(self, other):
        return self.year > other.year or (self.year == other.year and (self.month > other.month or (self.month ==
other.month and self.day > other.day)))

    def __str__(self):
        s = "{0} {1} {2}".format(self.day, self.month, self.year)
        return s

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, value):
        if self.tail == None:
            self.head = self.tail = Node(value)
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def compare_date(self):
        current = self.head
        res = self.head
        current = current.next

        while (current):
            if current.data.check_last(res.data):
                res = current
            current = current.next
        return res


value = LinkedList()

n = int(input())
for i in range(n):
    date, month, year = list(map(int, input().split(" ")))
    value.insert_tail(Time(date, month, year))

res = value.compare_date()
if res:
    print(res.data)
else:
    print(0)

