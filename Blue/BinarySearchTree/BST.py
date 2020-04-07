def binarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binarySearchRecursive(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid;
        if a[mid] > x:
            return binarySearchRecursive(a, left, mid - 1, x)
        return binarySearchRecursive(a, mid + 1, right, x)
    return -1


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


def bsLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == right or x < a[mid + 1]) and a[mid] == x:
            return mid
        elif x < a[mid]:
            return bsLast(a, left, mid - 1, x)
        else:
            return bsLast(a, mid + 1, right, x)
    return -1