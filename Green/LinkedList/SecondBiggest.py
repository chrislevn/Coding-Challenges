from collections import Counter

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

    def check_second(self):
        current = self.head
        arr = []
        while current:
            arr.append(current.data)
            current = current.next

        count_arr = Counter(arr)
        count = 0
        for i in count_arr:
            count += 1
        if count == 1:
            print(-1)
            exit()

        max_value = max(arr)
        arr.remove(max_value)
        print(max(arr))


value = LinkedList()

while (True):
    n = float(input())
    if n == -1:
        break
    value.insert_tail(n)


value.check_second()

