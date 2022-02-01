def minRange(letter, compareLetter): 
    firstGap = abs(ord(letter) - ord(compareLetter))
    if 25 - firstGap > firstGap: 
        return firstGap
    else: 
        return 25 - firstGap


t = int(input())

for i in range(t): 
    s = input()
    f = input()
    
    
    totalOperations = 0

    for a in s: 
        totalMin = 1000000000
        for b in f:
            totalMin = min(totalMin, minRange(a, b))
        totalOperations += totalMin
    print("Case #{}: {}".format(i+1, totalOperations))