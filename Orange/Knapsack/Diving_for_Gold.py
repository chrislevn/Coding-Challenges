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

def print_items(items, W, w): 
    count = 0 
    result = []
    for i in range(len(items)-1, 0, -1): 
        if K[i][W] != K[i-1][W]: 
            count += 1
            result.append((items[i].weight // (3*w), items[i].profit))
            W -= items[i].weight
    return count, result
            
            
if __name__ == '__main__': 
    flag = False
    while True: 
        try:
            if flag:
                space = input()
            flag = True
            
            t, w = map(int, input().split())
            num_treasures = int(input())
            
            items = [Item(0,0)]
            for i in range(num_treasures): 
                d, v = map(int, input().split())
                descent_time = w * d
                ascent_time= 2 * w * d
                total_time = descent_time + ascent_time
                
                items.append(Item(v, total_time))
                
            print(Knapsack(items, t))
            count_result, result_items = print_items(items, t, w)
            print(count_result)
            
            for item in result_items[::-1]:
                print(item[0], item[1])
                        
        except EOFError: 
            exit() 
        