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
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def delete_first(self):

        if self.head ==  None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next

    def print_and_check(self):
        current = self.head

        while current is not None:
            print(current.data, end=' ')
            current = current.next


value = LinkedList()

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    if len(x) == 1:
        value.delete_first()
    else:
        y = x[1]
        value.insert_tail(y)


value.print_and_check()