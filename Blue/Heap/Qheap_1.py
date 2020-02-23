import queue

class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

pq = queue.PriorityQueue()
pq_check = queue.PriorityQueue()

q = int(input())
for i in range(q):
    value = list(map(int, input().split()))

    if value[0] == 1:
        pq.put(value[1])

    if value[0] == 2:
        pq_check.put(value[1])

    if value[0] == 3:

        while not pq_check.empty() and pq.queue[0] == pq_check.queue[0]:
            pq.get()
            pq_check.get()

        print(pq.queue[0])
