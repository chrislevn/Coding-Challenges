class StructureStudent:
    def __init__(self, name_pos=0, first_point=1, second_point=2):
        self.name = name_pos
        self.first = first_point
        self.second = second_point

    def average_compute(self):
        average_result = (p1.first + p1.second) / 2
        return average_result


n = int(input())
arr = []
count = 0

for i in range(n):
    name_input = input()
    first_score, second_score = map(float, input().split())

    p1 = StructureStudent(name_input, first_score, second_score)
    average = p1.average_compute()

    arr.append(average)

#print(arr)

for j in range(len(arr)):
    if arr[j] >= 9.0:
        count += 1

print(count)
