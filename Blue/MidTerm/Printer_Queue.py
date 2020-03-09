import queue

# class PQEntry:
#     def __init__(self, value):
#         self.value = value
#
#     def __lt__(self, other):
#         return self.value > other.value

count = 1
p = queue.Queue()
# pq = queue.PriorityQueue()

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    bot = 0
    res = 0

    while True:
        Flag = True
        for i in range(bot + 1, len(arr)):
            if arr[i] > arr[bot]:
                arr.append(arr[bot])
                bot += 1
                if m < bot:
                    m = len(arr) - 1
                Flag = False

        if not Flag:
            continue

        if m == bot:
            print(res + 1)
            break

        bot += 1
        res += 1
