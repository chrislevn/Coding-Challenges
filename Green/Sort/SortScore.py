n, k = map(int, input().split())
number_arr = []
score_arr = []
check_arr = []
number_result = 0

for i in range(n):
    a, b = map(float, input().split())
    number_arr.append(a)
    score_arr.append(b)


def check_repeat(array):
    max_num = max(array)
    for i in range(len(array)):
        if array[i] == max_num:
            number_result = int(number_arr[i])
            check_arr.append(number_result)
    print(min(check_arr))
    check_arr.remove(min(check_arr))


for i in range(k):
    max_score_index = score_arr.index(max(score_arr))
    number_result = number_arr[max_score_index]
    check_repeat(score_arr)
    score_arr.remove(max(score_arr))
    number_arr.remove(number_result)
