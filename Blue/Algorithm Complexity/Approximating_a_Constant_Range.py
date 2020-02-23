from collections import Counter as co

n = int(input())
arr = list(map(int, input().split()))

curr = arr[0]
l, r = 0, 1
set_arr = []


class Node:
    def __init__(self, a = 0, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        s = "{0} {1}".format(self.a, self.b)
        return s



while l < len(arr) - 1 and r < len(arr):
    curr_arr = []
    curr_arr.append(arr[l])
    curr_arr.append(arr[r])

    count_arr = co(curr_arr)
    #print(len(count_arr))
    print()

    # print(l, r)
    print(arr[l], arr[l])

    if len(count_arr) <= 2 and abs(curr_arr[0] - curr_arr[1]) <= 1:
        print("Okay")
        r += 1
        set_arr.append(Node(l + 1, r + 1))

    else:
        l += 1

for i in range(len(set_arr)):
    print("result", set_arr[i])

result = set_arr[0].b - set_arr[0].a + 1

for i in range(1, len(set_arr)):
    if set_arr[i].b - set_arr[i].a + 1 > result:
        result = set_arr[i].b - set_arr[i].a + 1

print(result)



