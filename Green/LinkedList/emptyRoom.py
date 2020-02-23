class Room:
    def __init__(self, code = 0, bill = 1, status = 2):
        self.code = code
        self.bill = bill
        self.status = status

    def __str__(self):
        s = "{0} {1}".format(self.code, self.bill)
        return s

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

    def check_room(self):
        current = self.head
        arr = []
        while current:
            if current.data.status == "0":
                arr.append(current.data)
            current = current.next

        for i in range(len(arr)):
            print(arr[i])


value = LinkedList()
n = int(input())
for i in range(n):
    code, bill, status = list(input().split())
    value.insert_tail(Room(code, bill, status))

value.check_room()
