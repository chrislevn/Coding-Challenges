letter = input()
count = 0

for i in letter:
    if i >= '0' and i <= '9':
        count += 1

print(count)