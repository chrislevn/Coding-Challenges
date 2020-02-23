n, m, x, y = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

class Node:
    def __init__(self, a = 0, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        s = "{0} {1}".format(self.a, self.b)
        return s


result_arr = []
i, j = 0, 0
while i < len(arr_A) and j < len(arr_B):
    left = arr_A[i] - x
    right = arr_A[i] + y

    if (left <= arr_B[j]) and (right >= arr_B[j]):
        result_arr.append(Node(i + 1, j + 1))
        i += 1
        j += 1
        continue

    if right < arr_B[j]:
        i += 1
        continue

    if left > arr_B[j]:
        j += 1
        continue

print(len(result_arr))
for i in range(len(result_arr)):
    print(result_arr[i])
