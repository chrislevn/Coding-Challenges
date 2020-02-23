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

    def check_last_five(self):
        current = self.head
        arr = []
        while current:
            value = current.data % 10
            if value != 5:
                arr.append(current.data)
            current = current.next
        print(*arr)


set_list = LinkedList()
n = int(input())
for i in range(n):
    x = int(input())
    set_list.insert_tail(x)

set_list.check_last_five()
