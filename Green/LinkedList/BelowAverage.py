class Node():
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, value):
        if self.tail == None:
            self.head = self.tail = Node(value)
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def check_below(self):
        current = self.head

        while current:
            if current.data < 5:
                print(current.data)

            current = current.next


value = LinkedList()
n = float(input())
while n != -1:
    value.insert_tail(n)
    n = float(input())

value.check_below()