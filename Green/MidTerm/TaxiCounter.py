n = int(input())
count = 0
count_second = 0
count_third = 0

for i in range(1, n+1):
    if i > 1 and i < 6:
        count_second += 1

    if i > 5:
        count_third += 1

count = 15000 + 13500 * count_second + 11000 * count_third
if count > 135000:
    count = count - (count * 10 / 100)
if n == 0:
    count = 0

print(int(count))

