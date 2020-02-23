n = int(input())


def check_first(num):
    if num < 10:
        return num
    return check_first(num // 10)


if n < 0:
    print(check_first(-n))
else:
    print(check_first(n))
