n = int(input())
arr = list(map(int, input().split()))


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[0:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

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


print(*merge_sort(arr))