import math


class Node:
    def __init__(self, x = 0):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, x):
        if self.tail == None:
            self.head = self.tail = Node(x)

            return

        self.tail.next = Node(x)
        self.tail = self.tail.next

    def primeCounter(self):
        result = 0
        current = self.head
        while current:
            if check_primary(current.data):
                result += 1
            current = current.next
        return result


def check_primary(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False

        return True
    else:
        return False


value = LinkedList()
n = int(input())
while n != -1:
    value.insertTail(n)

    n = int(input())

print(value.primeCounter())
