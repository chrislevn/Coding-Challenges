class Node:
    def __init__(self, x = None):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, data):
        value = Node(data)
        if self.head == None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value


    def minimum(self):
        if self.head == None:
            return None
        current = self.head
        min_value = self.head
        while current:
            if current.data < min_value.data:
                min_value = current
            current = current.next
        return min_value



value = LinkedList()

while (True):
    x = int(input())
    if x == 0:
        break
    value.insertTail(x)

min_result = value.minimum()
if min_result:
    print(min_result.data)
else:
    print(0)