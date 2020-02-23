class Node:
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

    # def insert_order(self):
    #     if self.head == None:
    #         return None

    def print_list(self):
        count = 1
        current = self.head
        while current:
            print(count, current.data, end=" ")
            current = current.next
            count += 1



value = LinkedList()

while True:
    n = int(input())
    if n == 0:
        break
    value.insert_tail(n)


# value.insert_order()
value.print_list()

