from math import ceil, log2
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
        seg_tree[index] = a[left]
        return 
    mid = (left + right) // 2
    build_tree(a, seg_tree, left, mid, 2 * index + 1)
    build_tree(a, seg_tree, mid + 1, right, 2 * index + 2)
    seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]
    
    
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
        a[pos] = value 
        seg_tree[index] = value 
        return 
    mid = (left + right) // 2
    if pos <= mid: 
        update_query(seg_tree, a, left, mid, 2 * index + 1, pos, value)
    else: # if pos > mid 
        update_query(seg_tree, a, mid+1, right, 2 * index + 2, pos, value)
    seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]            
 
    
def sum_range(seg_tree, left, right, fr, to, index): 
    """
    Find sum of a range
    
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
        return 0 
    
    mid = (left + right) // 2
    left_node = sum_range(seg_tree, left, mid, fr, to, 2 * index + 1)
    right_node = sum_range(seg_tree, mid + 1, right, fr, to, 2 * index + 2)
    return left_node + right_node


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        n, q = map(int, input().split())
        n_arr = list(map(int, input().split()))
        
        n = len(n_arr)
        h = ceil(log2(n)) # log2: log base 2
        size_tree = 2 * (2**h) - 1
        seg_tree = [0] * size_tree
        build_tree(n_arr, seg_tree, 0, n - 1, 0)
        
        print("Case {}:".format(i + 1))
        
        for j in range(q):
            temp = list(map(int, input().split()))
            
            if temp[0] == 1: 
                pos_i = temp[1]
                print(n_arr[pos_i])
                update_query(seg_tree, n_arr, 0, n - 1, 0, pos_i, 0)
            if temp[0] == 2: 
                pos_i = temp[1]
                amount_v = temp[2]
                current_v = n_arr[pos_i]
                update_query(seg_tree, n_arr, 0, n - 1, 0, pos_i, current_v + amount_v)
            if temp[0] == 3: 
                pos_i = temp[1]
                pos_j = temp[2]
                print(sum_range(seg_tree, 0, n-1, pos_i, pos_j, 0))
                
           