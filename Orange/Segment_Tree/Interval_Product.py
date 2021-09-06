from math import ceil, log2, pow
INF = 10**9


def build_tree(a, seg_tree, left, right, index): 
    """
    Create segment tree
    
    Args: 
        a (list): list of initial values
        seg (tree): segment tree
        left (int): left index
        right (int): right index
        index (int): current index
    
    """
    
    if left == right: 
        if a[left] < 0:
            seg_tree[index] = -1
        elif a[left] > 0: 
            seg_tree[index] = 1
        else: 
            seg_tree[index] = 0
        return 
    mid = (left + right) // 2
    build_tree(a, seg_tree, left, mid, 2 * index + 1)
    build_tree(a, seg_tree, mid + 1, right, 2 * index + 2)
    seg_tree[index] = seg_tree[2 * index + 1] * seg_tree[2 * index + 2]
    
    
def update_query(seg_tree, a, left, right, index, pos, value): 
    """
    Update query 
    
    Args: 
        seg_tree (tree): segment tree 
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position 
        index (int): current index 
        pos (int): current position 
        value (int): finding value 
    
    """
    
    if pos < left or right < pos: 
        return 
    if left == right: 
        if value > 0: 
            a[pos] = 1 
            seg_tree[index] = 1 
        elif value < 0: 
            a[pos] = -1 
            seg_tree[index] = -1    
        else: 
            a[pos] = 0 
            seg_tree[index] = 0 
        return 
    mid = (left + right) // 2
    if pos <= mid: 
        update_query(seg_tree, a, left, mid, 2 * index + 1, pos, value)
    else: # if pos > mid 
        update_query(seg_tree, a, mid+1, right, 2 * index + 2, pos, value)
    seg_tree[index] = seg_tree[2 * index + 1] * seg_tree[2 * index + 2]            
 
    
def product_range(seg_tree, left, right, fr, to, index): 
    """
    Find product of a range
    
    Args: 
        seg_tree (tree): segment tree 
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position 
        index (int): current index 
        
    Returns: 
        sum value of a range
    
    """
    if fr <= left and to >= right: 
        return seg_tree[index]
    if fr > right or to < left: 
        return 1
    
    mid = (left + right) // 2
    left_node = product_range(seg_tree, left, mid, fr, to, 2 * index + 1)
    right_node = product_range(seg_tree, mid + 1, right, fr, to, 2 * index + 2)
    
    return left_node * right_node


if __name__ == '__main__': 
    while True:
        try:
            n, k = map(int, input().split())
            n_arr = list(map(int, input().split()))
            n = len(n_arr)
            h = int(ceil(log2(n)))
            size_tree = 2 * int(pow(2, h)) - 1
            seg_tree = [0] * size_tree # seg_tree with 0 when not with min problem
            build_tree(n_arr, seg_tree, 0, n - 1, 0)
            
            result = ''
            for i in range(k): 
                temp = input().split(' ')
                command = temp[0]
                first = int(temp[1])
                second = int(temp[2])
                
                if command == "C": 
                    update_query(seg_tree, n_arr, 0, n-1, 0, first-1, second)
                if command == "P": 
                    temp_res = product_range(seg_tree, 0, n-1, first-1, second-1, 0)             
                    if temp_res > 0: 
                        result += "+"
                    elif temp_res < 0: 
                        result += "-"
                    else: 
                        result += "0"
            print(result)
        except EOFError: 
            exit()