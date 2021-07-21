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
            
# Multiple Knapsack
class Item: 
    def __init__(self, profit=0, weight=0):
        self.profit = profit
        self.weight = weight 
        
K = []

def unbounded_knapsack(items, W): 
    global K
    K = [0] * (W + 1)
    for i in range(0, W + 1): 
        for j in range(len(items)): 
            if items[j].weight <= i: 
                K[i] = max(K[i], items[j].profit + \
                    K[i - items[j].weight])
    return K[W]

## Sample item: items = [Item(1, 1), Item(2, 2)]

# Fractional Knapsack
class Item_Fractional: 
    def __init__(self, profit=0, weight=0): 
        self.profit = profit
        self.weight = weight
    def __lt__(self, other): 
        r1 = self.profit / self.weight
        r2 = other.profit / other.weight 
        return r1 > r2
    
def fractional_knapsack(items, W): 
    items.sort()
    cur_weight = 0 
    final_profit = 0 
    for i in range(len(items)): 
        if cur_weight + items[i].weight <= W: 
            cur_weight += items[i].weight 
            final_profit += items[i].profit 
        else: 
            re_weight = W - cur_weight
            final_profit += items[i].profit * (re_weight / items[i].weight) 
            break

        