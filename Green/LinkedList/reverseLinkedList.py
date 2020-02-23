class Node:
    def __init__(self, data = 0):
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

    def print_reverse(self):
        current = self.head
        arr = []
        while current:

            arr.append(current.data)
            current = current.next

        arr = arr[::-1]
        for i in arr:
            print(i)


value = LinkedList()
n = int(input())
while n != 0:
    value.insert_tail(n)
    n = int(input())

value.print_reverse()