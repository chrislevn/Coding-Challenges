import math

n = int(input())
arr = list(map(int, input().split()))
prime_arr = []
prime_index = []
not_prime = []
new_arr = []
not_prime_index = []


def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False

        return True
    else:
        return False


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            if not is_prime(key):
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
    return array


for i in range(len(arr)):
    if is_prime(arr[i]):
        prime_index.append(i)
        prime_arr.append(arr[i])

for i in range(len(arr)):
    if arr[i] not in prime_arr:
        not_prime.append(arr[i])
        not_prime_index.append(i)

new_arr = insertion_sort(not_prime)

count_not_prime = 0
count_prime = 0


for i in not_prime_index:
    arr[i] = not_prime[count_not_prime]
    count_not_prime += 1

for i in prime_index:
    arr[i] = prime_arr[count_prime]
    count_prime += 1

print(*arr)
