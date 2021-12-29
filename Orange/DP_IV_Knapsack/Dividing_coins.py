# 0/1 Knapsack
class Item: 
    def __init__(self, profit=0, weight=0):
        self.profit = profit
        self.weight = weight 
        
K = []

def Knapsack(items, W):
    global K
    K = [[0] * (W + 1) for i in items]
    for i in range(1, len(items)): 
        for j in range(W + 1): 
            if items[i].weight > j: 
                K[i][j] = K[i-1][j]
            else: 
                temp1 = items[i].profit + K[i-1][j-items[i].weight]
                temp2 = K[i-1][j]
                K[i][j] = max(temp1, temp2)    
    return K[len(items) - 1][W]

def print_items(items, W): 
    # print("List Items: ")
    result = []
    for i in range(len(items)-1, 0, -1): 
        if K[i][W] != K[i-1][W]: 
            result.append(i-1)
            W -= items[i].weight
    return result

if __name__ == '__main__': 
    n = int(input())
    for i in range(n): 
        m = int(input())
        items = [Item(0,0)]
        arr = list(map(int, input().split()))
        for j in range(len(arr)): 
            items.append(Item(arr[j], arr[j]))
        
        half_value = sum(arr) // 2
        
        first_sum = Knapsack(items, half_value) 
        
        check = print_items(items, half_value)
        other_sum = 0
        
        for j in range(len(arr)): 
            if j not in check: 
                other_sum += arr[j]
        
        print(abs(first_sum - other_sum))
            