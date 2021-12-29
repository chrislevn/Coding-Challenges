def main():
    values = input().split()

    n = int(values[0])
    m = int(values[1])

    factors = []
    result = []
    for i in range(2, n+2):
        factors.append(int(values[i]))

    for i in range(n+2, len(values)):
        num = int(values[i])
        found = False
        for fac in factors:
            if num % fac == 0:
                if found == False:
                    result.append(num)
                    found = True


    st = ""
    for num in result:
        st = st + str(num) + " "

    st = st[:-1]
    print(st)



main()