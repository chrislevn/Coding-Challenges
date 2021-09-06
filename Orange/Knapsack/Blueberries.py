class Item: 
    def __init__(self, profit=0, weight=0):
        self.profit = profit
        self.weight = weight 
        
K = []


def Knapsack(items, W):
    global K
    K = [[0] * (W + 1) for i in items]
    for i in range(items[1].weight, W +1): 
        K[1][i] = items[1].weight
    for i in range(2, len(items)): 
        for j in range(W + 1): 
            if items[i].weight > j: 
                K[i][j] = K[i-1][j]
            else: 
                temp1 = items[i].profit + K[i-2][j-items[i].weight]
                temp2 = K[i-1][j]
                K[i][j] = max(temp1, temp2)    
    return K[len(items) - 1][W]


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        n, k = map(int, input().split())
        n_arr = list(map(int, input().split()))
        
        items = [Item(0, 0)]
        for value in n_arr: 
            items.append(Item(value, value))
        
        print("Scenario #{}: {}".format(i+1, Knapsack(items, k)))
