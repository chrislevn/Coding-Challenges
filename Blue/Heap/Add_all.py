import queue


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


n = int(input())

pq = queue.PriorityQueue()

while n != 0:
    arr = list(map(int, input().split()))

    for i in arr:
        pq.put(i)

    sum_value = 0
    result = 0

    for i in range(len(arr) - 1):
        value_1 = pq.get()
        value_2 = pq.get()
        sum_value = value_1 + value_2
        result += sum_value

        pq.put(sum_value)
    pq.get()

    print(result)

    n = int(input())
# 2, 4, 6 ,7 9h30
# thu 7