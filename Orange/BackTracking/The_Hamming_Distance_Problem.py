def permutations(n, h, num1, start, res):
    """Permutate the order of binary string. 
    Append any accepted permutation into result list

    Args:
        n: number of digits
        h: number of accepeted 1s
        num1: number of current 1s
        start: current index
        res: current binary string list
    """
    if num1 == h: 
        print(''.join(res))
        return 
    for i in range(n - h + num1, start - 1, -1):
        res[i] = '1'
        permutations(n, h, num1 + 1, i + 1, res)
        res[i] = '0'    #reset to 0
            

if __name__ == "__main__":
    t = int(input())

    for i in range(t): 
        blank = input()

        n, h = map(int, input().split())
        result = []
        temp_arr = ["0"]*n

        permutations(n, h, 0, 0, temp_arr)
        
        for value in result: 
            print(value)

        if i < t-1:
            print()
