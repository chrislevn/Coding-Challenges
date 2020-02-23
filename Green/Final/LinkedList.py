arr = []
result = []

from collections import Counter as co

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

    def check_intersect(self):
        current = self.head
        flag = False
        index_value = 0
      
        while current:
            while index_value < len(arr) and current.data > arr[index_value]: 
                index_value += 1
            if index_value < len(arr) and current.data == arr[index_value]:
                flag = True 
                result.append(current.data)

            current = current.next 

        if flag == False: 
            print("NO INTERSECTION")
            exit()
        print(*co(result))
      


value = LinkedList()
n = int(input())

while n != -1:
    arr.append(n)
    n = int(input()) 
   
m = int(input())

while m != -1:
  value.insert_tail(m)
  m = int(input())

value.check_intersect()