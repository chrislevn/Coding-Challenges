def solve(n): 
    if n in result: 
        return result[n]
    else: 
        result[n] = max(n, solve(n // 2) + solve(n // 3) + solve(n // 4))
        return result[n]


if __name__ == '__main__': 
    while True:
        try: 
            n = int(input())
            result = {0:0, 1:1}
            print(solve(n))
        except EOFError: 
            break
            