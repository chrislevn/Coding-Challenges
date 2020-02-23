n = int(input())
arr = []
flag = True

for i in range(n):
    letter = input()
    letter = letter.lower()
    for j in letter:
        if j == "b" or j == "i" or j == "g" or j == "o":
           flag = True
           break
        else:
            flag = False

    if flag:
        arr.append("YES")
    else:
        arr.append("NO")

print(*arr, sep="\n")








