import string
string.ascii_lowercase

alphabet_arr = list(string.ascii_lowercase)
m = list(input())
n = list(input())


def check_strings(m, n):
    m = m[::-1]
    new_arr = []
    x = 1

    if len(m) != 1:
        for i in range(len(m)):
            if m[i] != 'z':
                next_element = alphabet_arr.index(m[i]) + x
                new_arr.append(alphabet_arr[next_element])
                x = 0
            elif m[i] == 'z' and x == 1:
                new_arr.append('a')
            else:
                new_arr.append('z')
            # new_arr.append(m[i])

        new_arr.reverse()
        new_arr = ''.join(new_arr)
        n = ''.join(n)

        if new_arr == n:
           print('No such string')
           return
        else:
           print(new_arr)
           return

    else:
        if alphabet_arr.index(m[0]) < alphabet_arr.index(n[0]):
            next_element = alphabet_arr.index(m[0]) + 1
            print(alphabet_arr[next_element])
            return


check_strings(m,n)



