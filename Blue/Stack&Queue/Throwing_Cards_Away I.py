import queue

n = int(input())
while n != 0:
    arr = queue.Queue()
    discard_arr = []

    for i in range(n):
        arr.put(i+1)

    count = 1
    while arr.qsize() > 1:
        if count % 2 != 0:
            discard_arr.append(arr.get())
        else:
            arr.put(arr.get())

        count += 1

    if len(discard_arr) >= 1:
        print('Discarded cards: ', end='')
        print(*discard_arr, sep=", ")
    else:
        print('Discarded cards:')

    print("Remaining card:", arr.get())
    n = int(input())

