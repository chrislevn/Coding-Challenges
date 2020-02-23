letter = input()
ans = ''
for i in range(len(letter)):
    if i >= 2 and letter[i - 2] == '.' and letter[i - 1] == ' ' and letter[i] >= 'a' and letter[i] <= 'z':
        ans += chr(ord(letter[i]) - ord('a') + ord('A'))
    else:
        ans += letter[i]
print(ans)