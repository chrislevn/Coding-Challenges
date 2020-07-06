def recursion(j): 
    i = 50
    if i == j:
        print("something")
        k = recursion(i)
        return 0
    else: 
        return 0

recursion(50)