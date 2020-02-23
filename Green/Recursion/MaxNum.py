n = int(input())


def check_max(num):
    if num < 10:
        return num
    outlier = num % 10
    return max(outlier, check_max(num // 10))

if n < 0:
    print(check_max(-n))
else:
    print(check_max(n))

