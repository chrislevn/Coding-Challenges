n = int(input())
arr = list(map(int, input().split()))

sort_reverse = sorted(arr)
sort_reverse.reverse()
# print(sort_reverse)


point_arr = []
for i in range(len(sort_reverse)):
    point_arr.append(i+1)
# print(point_arr)

rank_arr = [1]
curr = sort_reverse[0]
for i in range(1, len(point_arr)):

    if sort_reverse[i] < curr:
        rank_arr.append(point_arr[i])

    if sort_reverse[i] == curr:
        rank_arr.append(point_arr[i-1])

    curr = sort_reverse[i]

# print(rank_arr)

result_arr = []

ranking = [0] * 2005

for i in range(len(arr)):
    point = sort_reverse[i]
    if not ranking[point]:
        ranking[point] = i + 1

for i in range(len(arr)):
    result_arr.append(ranking[arr[i]])

print(*result_arr)


