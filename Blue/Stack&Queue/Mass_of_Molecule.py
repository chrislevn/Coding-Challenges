formula = input()
result = 0
new_arr = []

for i in range(len(formula)):

    if formula[i] == "C":
        new_arr.append(12)
    if formula[i] == "O":
        new_arr.append(16)
    if formula[i] == "H":
        new_arr.append(1)
    if formula[i].isnumeric():
        if formula[i-1] != ")":
            new_arr.append(new_arr.pop() * int(formula[i]))
        else:
            new_arr.append(new_arr.pop() * int(formula[i]))

    if formula[i] == "(":
        new_arr.append("(")
    if formula[i] == ")":
        sub_list = []
        while new_arr[-1] != "(":
            sub_list.append(new_arr.pop())
        new_arr.pop()
        new_arr.append(sum(sub_list))

print(sum(new_arr))
