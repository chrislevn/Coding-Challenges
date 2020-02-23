import queue


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


pq = queue.PriorityQueue()
min_pq = queue.PriorityQueue()
n = int(input())
numReviews = 0

for i in range(n):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        numReviews += 1
        # pq.put(PQEntry(arr[1]))
        topThreeCheck = numReviews // 3

        # maxValue = pq.queue[0]

        minSize = min_pq.qsize()
        if min_pq.qsize() > 0 and arr[1] > min_pq.queue[0]:
            pq.put(PQEntry(min_pq.get()))
            min_pq.put(arr[1])

        else:
            pq.put(PQEntry(arr[1]))

        if topThreeCheck > minSize:
            min_pq.put(pq.get().value)

    if arr[0] == 2:
        if min_pq.qsize() < 1:
            print("No Reviews Yet")
        else:
            print(min_pq.queue[0])
