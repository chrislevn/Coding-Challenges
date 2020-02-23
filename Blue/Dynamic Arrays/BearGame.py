n = int(input())
x = [int(i) for i in input().split()]

def check_interest(array):
    current = 0

    if array[0] > 15:
        print(current + 15)
        return
    else:
        for i in range(len(array)):
            next = array[i] - current
            current = array[i]

            if (next > 15):
                total = array[i-1] + 15
                print(total)
                return

            else:
                total = current + 15
                if total > 90:
                    print(90)
                    return


        print(total)


check_interest(x)
