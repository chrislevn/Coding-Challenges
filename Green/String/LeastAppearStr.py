import collections as co

n = int(input())
arr = []
new_arr = []

for i in range(n):
    letter = input()
    letter = letter.lower()

    for j in letter:
        new_value = ord(j)
        arr.append(new_value)

    arr.sort()
    for m in arr:
        new_arr.append(chr(m))


    a = co.Counter(new_arr)
    print(min(a, key=a.get).upper())
    new_arr.clear()
    arr.clear()