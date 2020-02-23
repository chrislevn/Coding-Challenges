n = int(input())

while n != 0:
    arr = list(map(int, input().split()))

    new_arr = []
    main_park = []
    check_arr = []

    id = 1
    count_id = 1
    i = 0

    while i < len(arr):
        while len(new_arr) > 0:
            if new_arr[-1] == id:
                main_park.append(new_arr.pop())
                id += 1
            else:
                break

        if arr[i] != id:
            new_arr.append(arr[i])
        else:
            main_park.append(arr[i])
            id += 1

        i += 1
        check_arr.append(count_id)
        count_id += 1

    for i in range(len(new_arr)):
        main_park.append(new_arr.pop())

    if main_park == check_arr:
        print("yes")
    else:
        print("no")

    n = int(input())

