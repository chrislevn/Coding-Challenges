import queue

class PQEntryMax:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


min_pq = queue.PriorityQueue()
max_pq = queue.PriorityQueue()

n = int(input())

change_arr = []

for i in range(n):
    bill_arr = []
    arr = list(map(int, input().split()))

    if len(arr) > 1:
        for j in range(1, len(arr)):
            bill_arr.append(arr[j])

    for i in bill_arr:
        min_pq.put(i)
        max_pq.put(PQEntryMax(i))

    max_value = max_pq.get().value
    min_value = min_pq.get()

    # print(bill_arr)
    # print(max_value, min_value)

    change = max_value - min_value

    # print(change)
    # print()

    change_arr.append(change)

print(sum(change_arr))