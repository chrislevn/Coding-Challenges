
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
    print("List Items: ")
    for i in range(len(items)-1, 0, -1): 
        if K[i][W] != K[i-1][W]: 
            print('[', items[i].profit, ',', \
                  items[i].weight, ']', sep='')
            W -= items[i].weight
            

if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        n, w = map(int, input().split())
        items = [Item(0,0)]
        for j in range(n): 
            c, p, t = map(int, input().split())
            items.append(Item(c*p,t))
        print(Knapsack(items, w))
        
            