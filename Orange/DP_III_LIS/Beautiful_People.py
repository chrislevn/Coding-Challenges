result = []
path = []
last = -1

def printLIS(a, increasing_sub, length): 
    i = increasing_sub[length-1]
    res = []
    while i > -1:
        res.append(a[i].id)
        i = path[i]
    res = res[::-1]
    
    return length, res
            
        
def LIS_double(a): 
    global last, result, path
    length = 0 
    path = [-1] * len(a)
    result = [1] * len(a)
    
    for i in range(1, len(a)): 
        for j in range(i): 
            if a[i][0] > a[j][0] and a[i][1] > a[j][1] and result[i] < result[j] + 1: 
                result[i] = result[j] + 1
                path[i] = j
                
    for i in range(len(a)): 
        if length < result[i]: 
            last = i 
            length = result[i]
            
    return result

def lower_bound(a, sub, n, x): 
    left = 0 
    right = n 
    pos = right 
    while left < right: 
        mid = left + (right - left) // 2
        index = sub[mid]
        
        if a[index].b >= x.b: 
            pos = mid 
            right = mid 
        else: 
            left = mid + 1
            
    return pos 


def LIS_binary_search_double(a): 
    global path 
    length = 1
    path = [-1] * len(a)
    result.append(0)
    
    for i in range(1, len(a)): 
        if a[i].b <= a[result[0]].b: 
            result[0] = i 
        elif a[i].b > a[result[length - 1]].b: 
            path[i] = result[length - 1]
            result.append(i)
            length += 1
        else: 
            pos = lower_bound(a, result, length, a[i])
            path[i] = result[pos - 1]
            result[pos] = i 
    return printLIS(a, result, length)


class Member: 
    def __init__(self, s, b, id): 
        self.s = s
        self.b = b
        self.id = id
        
    def __lt__(self, other): 
        if self.s == other.s:
            return self.b > other.b 
        return self.s < other.s
    
    def __str__(self):
        return str(self.s) + " " + str(self.b) + " " + str(self.id)
    

if __name__ == '__main__': 
    n = int(input())
    arr = []
    for i in range(n): 
        s, b = map(int, input().split())
        arr.append(Member(s, b, i+1))
        
    arr = sorted(arr)
        
    final_res =LIS_binary_search_double(arr)
    print(final_res[0])
    print(*final_res[1])
    