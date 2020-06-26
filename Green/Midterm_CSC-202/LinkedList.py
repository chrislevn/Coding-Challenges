class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.value = None
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            self.head.next = Node(value)
            self.head = self.head.next


lk = LinkedList()
value1 = 5
lk.add(value1)

print(lk.value)