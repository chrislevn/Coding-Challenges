import queue

class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


n = int(input())
arr = list(map(int, input().split()))

pq = queue.PriorityQueue()

for x in arr:
    pq.put(PQEntry(x))

    second = 0
    third = 0
    result = 1

    length = len(pq.queue)

    if length <= 2:
        print(-1)

    else:
        process = []

        for i in range(3):
            num = pq.get()
            process.append(num)

        for i in process:
            pq.put(i)

        for i in process:
            result = result * i.value

        print(result)
