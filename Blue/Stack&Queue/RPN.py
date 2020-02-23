import string
import queue

alpha_list = list(string.ascii_lowercase)
operand = ["+", "-", "*", "/","^"]

t = int(input())

for i in range(t):
    letters = list(input())
    operand_list = []
    letter_list = []
    result_list = []

    for j in letters:
        if j.isalpha():
            result_list.append(j)
        if j in operand:
            operand_list.append(j)
        else:
            if j == ")":
                result_list.append(operand_list.pop())

    print(*result_list, sep="")



