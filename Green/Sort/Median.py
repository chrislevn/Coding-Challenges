n = int(input())
arr = list(map(int, input().split()))
new_arr = []


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


new_arr = insertion_sort(arr)
arr_len = len(new_arr)
index = len(new_arr) // 2

if arr_len % 2 == 0:
    left = index - 1
    result = (new_arr[left] + new_arr[index]) / 2
    print(result)
else:
    print(new_arr[index])
