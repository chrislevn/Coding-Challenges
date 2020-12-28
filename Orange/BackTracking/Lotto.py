x = 6
k = 0
b = [None] * 6
a = []

def solve(index, curPosArray):
    global b, x, k
    #for j: những phần tử phía sau luôn lớn hơn những phần tử nằm trước
    for j in range(curPosArray, k - x + index + 1):
        b[index] = arr[j]
        if index == x - 1:
            print(*b)
        else:
            solve(index + 1, j + 1)

if __name__ == "__main__":
    k, *arr = list(map(int, input().split()))
    while k != 0:
        solve(0, 0)
        print()
        k, *arr = list(map(int, input().split()))
