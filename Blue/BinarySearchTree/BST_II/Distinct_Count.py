t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    s = set(arr)

    if len(s) < x:
        print("Bad")
    elif len(s) == x:
        print("Good")
    else:
        print("Average")