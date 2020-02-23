n_a, n_b = map(int, input().split())
k, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))


def check_array(n_a, n_b, k, m, arr_a, arr_b):
    if arr_a[k-1] < arr_b[n_b - m]:
        print('YES')
    else:
        print('NO')


check_array(n_a, n_b, k, m, arr_a, arr_b)






