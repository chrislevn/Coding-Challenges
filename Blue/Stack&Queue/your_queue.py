import queue

p, c = map(int, input().split())
count = 0

while p != 0 or c != 0:
    count += 1
    arr = queue.Queue()
    order_arr = []

    for i in range(min(p, c)):
        arr.put(i+1)

    for i in range(c):
        command = list(input().split(" "))

        if command[0] == "N":
            n = arr.get()
            order_arr.append(n)
            arr.put(n)

        if command[0] == "E":
            index_value = int(command[1])
            arr.put(index_value)

            for j in range(arr.qsize() - 1):
                m = arr.get()
                if m != index_value:
                    arr.put(m)

    print("Case " + str(count) + ":")
    for i in order_arr:
        print(i)
    p, c = map(int, input().split())



