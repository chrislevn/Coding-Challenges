from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = len(arr) - 1

count_arr = Counter(arr)
if int(len(count_arr)) < int(k):
    print(-1, - 1)
    exit()

if k == 1:
    print(1, 1)
    exit()


def check_array(array, left, right, k):
    check_left = False
    count = [0] * (10 ** 5 + 1000)
    number_unique = 0

    for i in range(len(array)):
        count[array[i]] += 1
        if count[array[i]] == 1:
            number_unique += 1

    while (True):
        if check_left == False:
            if number_unique > k:
                count[array[left]] -= 1
                if count[array[left]] == 0:
                    number_unique -= 1
                left += 1
            elif number_unique == k:
                count[array[left]] -= 1
                if count[array[left]] == 0:
                    number_unique -= 1
                left += 1
            elif number_unique < k:
                left -= 1
                count[array[left]] += 1
                if count[array[left]] == 1:
                    number_unique += 1

                check_left = True
                continue

        if check_left == True:
            if number_unique == k:
                count[array[right]] -= 1
                if count[array[right]] == 0:
                    number_unique -= 1
                right -= 1
            if number_unique < k:
                right += 1
                count[array[right]] += 1
                if count[array[right]] == 1:
                    number_unique -= 1

                break

    print(left + 1, right + 1)


check_array(arr, left, right, k)
