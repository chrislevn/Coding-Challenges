import collections as co

arr = []
check_row = []
small_arr = []
new_arr = []
other_arr = []
result = True

for i in range(9):
    temp = list(map(int, input().split()))
    arr.append(temp)

transpose_arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]


def check_matrix(array):
    start, end = 0, 3
    for j in range(3):
        start_2, end_2 = 0, 3

        for m in range(3):
            new_arr.clear()
            for i in array[start:end]:
                new_arr.append(i[start_2: end_2])

            if not check_arr(new_arr):
                return False

            start_2 += 3
            end_2 += 3

        if not check_arr(new_arr):
            return False
        start += 3
        end += 3
        new_arr.clear()
    return True


def check_arr(array):
    small_arr.clear()
    for i in range(len(array)):
        for j in array[i]:
            small_arr.append(j)

    a = co.Counter(small_arr)
    for j in range(10):
        if a[j] > 1:
            return False
    return True


def check_row(row_arr):
    for i in range(len(row_arr)):
        a = co.Counter(row_arr[i])
        for j in range(10):
            if a[j] > 1:
                return False
    return True


if check_row(arr) and check_row(transpose_arr) and check_matrix(arr):
    print("YES")
else:
    print("NO")