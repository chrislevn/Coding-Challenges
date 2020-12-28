def check_boring(number): 
    number = str(number)

    for ch in range(len(number)):
        if (ch + 1)  % 2 != 0 and int(number[ch]) % 2 == 0: 
            return False
        elif (ch + 1)  % 2 == 0 and int(number[ch]) % 2 != 0: 
            return False
    
    return True 

if __name__ == "__main__":
    t = int(input())

    for i in range(t): 
        l, r = map(int, input().split())

        result = 0

        for num in range(l, r+1): 
            if (num | 5) % 2 == 0: 
                result += 1
        print("Case #{}: {}".format(i+1, result))