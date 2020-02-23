n = int(input())
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
new_arr = []
index_even_arr = []
index_odd_arr = []


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def merge_decrease_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[0:mid]
    right = array[mid:]

    merge_decrease_sort(left)
    merge_decrease_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


for i in range(len(arr)):
    if arr[i] % 2 == 0:
        index_even_arr.append(i)
    else:
        index_odd_arr.append(i)

for i in index_even_arr:
    even_arr.append(arr[i])

for i in index_odd_arr:
    odd_arr.append(arr[i])

even_arr = insertion_sort(even_arr)
odd_arr = merge_decrease_sort(odd_arr)

count_even = 0
count_odd = 0


for i in index_even_arr:
    arr[i] = even_arr[count_even]
    count_even += 1

for i in index_odd_arr:
    arr[i] = odd_arr[count_odd]
    count_odd += 1

print(*arr)




