t = int(input())

for i in range(t): 
    n, m = map(int, input().split())
    power = []
    i = 0
    
    while m: 
        if m & 1: 
            power.append(i)
        m >>= 1
        i += 1

    print(' + '.join('({}<<{})'.format(n, power) for power in reversed(power)))