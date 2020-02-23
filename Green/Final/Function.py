a = int(input())
b = int(input())
c = int(input())

arr = []

result_1 = a + b +c
result_2 = a * b + c
result_3 = a + b * c
result_4 = (a + b) * c
result_5 = a * (b + c)
result_6 = a * b * c

arr.append(result_1)
arr.append(result_2)
arr.append(result_3)
arr.append(result_4)
arr.append(result_5)
arr.append(result_6)

print(max(arr))
