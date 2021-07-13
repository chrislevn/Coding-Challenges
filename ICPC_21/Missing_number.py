# import re
# def getMissingNum(a, n): 
#     x1 = a[0]
#     x2 = 1
     
#     for i in range(1, n):
#         x1 = x1 ^ a[i]
         
#     for i in range(2, n + 2):
#         x2 = x2 ^ i
     
#     return x1 ^ x2

# if __name__ == "__main__":
#     n = int(input())
#     arr = input()
#     test = re.findall('.{1}', arr)
#     # arr = [int(i) for i in str(arr)]
#     # # print(arr)

#     # res = getMissingNum(arr, len(arr))
#     print(test)

if __name__ == "__main__":
    n = int(input())
    input = input()
    done = False

    num = 1
    for i in range(9):
        current = int(input[i])
        if num != current:
            print(num)
            done = True
            exit()
        num+=1

    if not done:
        input = input[9:]

    for i in range(0, len(input), 2):
        current = int(input[i]) * 10 + int(input[i+1])
        if num != current:
            print(num)
            done = True
            exit()
        num+=1

    if not done:
        print(100)
