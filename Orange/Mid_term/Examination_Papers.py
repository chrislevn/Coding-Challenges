# import sys
# sys.setrecursionlimit = 1e9

# def TowerOfHanoi(n , source, destination, auxiliary):
#     global step
#     if n==1:
#         # print("Move disk 1 from source",source,"to destination",destination)
#         step += 1
#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     # print("Move disk",n,"from source",source,"to destination",destination)
#     step += 1
#     TowerOfHanoi(n-1, auxiliary, destination, source)

def modular_exponention(a, b, m): 
    result = 1
    a %= m 
    while b > 0: 
        if b % 2 == 1: 
            result = (result * a) % m 
        
        b //= 2
        a = (a * a) % m 
    
    return result

if __name__ == "__main__": 
    t = int(input())
    for i in range(t): 
        n = int(input())
        step = modular_exponention(2, n, int(1e9 + 7)) - 1

        if step == -1:
            step += int(1e9 + 7)
        # TowerOfHanoi(n,'A','B','C')
        print(step)