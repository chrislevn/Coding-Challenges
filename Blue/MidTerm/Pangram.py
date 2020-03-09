import string
letter_arr = string.ascii_lowercase

visited = [0] * 100

n = int(input())
letter = input()

if n < 26:
    print("NO")
else:
    for i in range(len(letter)):
        if letter[i] in letter_arr:
            visited[i] = 1

    if sum(visited) >= 26:
        print("YES")
