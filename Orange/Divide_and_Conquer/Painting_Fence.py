import sys 
sys.setrecursionlimit(int(10e5))

def strokesNeeded(left, right, paitned_height): 
    if left > right: 
        return 0 

    mini = left 
    for i in range(left, right+1): 
        if a[i] < a[mini]: 
            mini = i

    all_vertical = right - left + 1

    left_side = strokesNeeded(left, mini - 1, a[mini])
    right_side = strokesNeeded(mini + 1, right, a[mini])
    combine = a[mini] - paitned_height + left_side + right_side
    
    return min(all_vertical, combine)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    print("{}".format(strokesNeeded(0, n-1, 0)))
