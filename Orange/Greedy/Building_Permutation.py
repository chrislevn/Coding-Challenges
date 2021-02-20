def building_permutation(arr, n): 
    temp_list = list(range(1, n+1))
    arr = sorted(arr)
    min_move = 0

    for i in range(len(temp_list)): 
        min_move += abs(temp_list[i] - arr[i])

    return min_move


if __name__ == "__main__": 
    n = int(input())
    arr = list(map(int, input().split()))   

    print(building_permutation(arr, n))
