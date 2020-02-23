n, s, r = map(int, input())
arr_s = list(map(int, input().split()))
arr_r = list(map(int, input().split()))

def check_number(num, check_num):
    if (num + 1) == check_num or (num - 1) == check_num:
        return True
    else:
        return False

for i in range(len(arr_r)):

