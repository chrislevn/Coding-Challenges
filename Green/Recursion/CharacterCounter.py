n = int(input())

def character_count(num):
    if num < 10:
        return 1
    return 1 + character_count(num // 10)

if n < 0:
    n = -n
    print(character_count(n))
else:
    print(character_count(n))
