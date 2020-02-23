n = int(input())
arr = list(map(int, input().split()))
n = len(arr)
new_arr = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        new_arr.append(arr[i])

print(sum(new_arr))




def sum_even(array, n):
    if n == 0:
        return 0
    else:
        if array[n - 1] % 2 == 0:
            return array[n - 1] + sum_even(array, n - 1)
        else:
            return sum_even(array, n - 1)


#print(sum_even(arr, n))
