n = int(input())
arr = []
s = dict()

for i in range(n):
    name = input()
    if name in s:
        s[name] += 1
    else:
        s[name] = 1

maxValue = 0
result = 0

for i in s:
    if s[i] > maxValue:
        maxValue = s[i]
        result = i

print(result)


