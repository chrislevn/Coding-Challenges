
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
            self.tail = self.head = Node(value)
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def print_index(self):
        current = self.head
        count = 0
        arr = []
        while current:
            count += 1
            if check_symmetry(current.data):
                arr.append(count - 1)

            current = current.next
        print(*arr)
                

def check_symmetry(value):
    value = list(value)

    for i in range(len(value)):
        if value[i] == value[-(i + 1)]:
            if i == len(value) - 1:
                return True
        else:
            return False


value = LinkedList()

while (True):
    n = input()
    if n == str(-1):
        break
    value.insert_tail(n)

value.print_index()



