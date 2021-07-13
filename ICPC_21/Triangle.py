from itertools import combinations 

def checkValidity(a, b, c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        

arr = []
n = int(input())
for i in range(n): 
    number = int(input())
    arr.append(number)
    
comb = combinations(arr, 3) 
result = 0
for item in list(comb): 
    if checkValidity(item[0], item[1], item[2]): 
        result += 1

print(result)

