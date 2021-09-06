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
    seg_tree[index] = min(seg_tree[2 * index + 1], seg_tree[2 * index + 2])
    

def min_range_lazy(seg_tree, lazy, left, right, fr, to, index):
    """Find min of a segment using lazy segment tree
    
    Args: 
        seg_tree (tree): segment tree
        lazy (tree): lazy segment tree
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position
        index (int): current index
    
    Returns: 
        minimum of a segment
    """
    if left > right: 
        return INF
    if lazy[index] != 0: 
        seg_tree[index] += lazy[index]
        if left != right: 
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index] 
        lazy[index] = 0
    
    if fr > right or to < left: 
        return INF
    if fr <= left and to >= right: 
        return seg_tree[index]
    mid = (left + right) // 2
    return min(min_range_lazy(seg_tree, lazy, mid + 1, right, fr, to, 2 * index + 2), 
               min_range_lazy(seg_tree, lazy, left, mid, fr, to, 2 * index + 1))


def update_query_min_range_lazy(seg_tree, lazy, left, right, fr, to, delta, index): 
    """
    Update query with minimum range and lazy segment tree
    
    Args: 
        seg_tree (tree): segment tree
        lazy (tree): lazy segment tree
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position
        delta (int): increasing amount 
        index (int): current index
            
    """
    
    if left > right: 
        return 
    if lazy[index] != 0: 
        seg_tree[index] += lazy[index]
        if left != right: 
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    # no overlap condition
    if fr > right or to < left: 
        return
    # total overlap condition 
    if fr <= left and right <= to: 
        seg_tree[index] += delta 
        if left != right: 
            lazy[2 * index + 1] += delta 
            lazy[2 * index + 2] += delta
        return 
    
    # otherwise partial overlap so look both left and right 
    mid = (left + right) // 2
    update_query_min_range_lazy(seg_tree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    update_query_min_range_lazy(seg_tree, lazy, mid + 1, right, fr, to, delta, 2 * index + 2)
    seg_tree[index] = min(seg_tree[2 * index + 1], seg_tree[2 * index + 2])


if __name__ == "__main__": 
    n = int(input())
    a_arr = list(map(int, input().split()))
    
    length = len(a_arr)
    h = ceil(log2(length)) # log2: log base 2
    size_tree = 2 * (2**h) - 1
    seg_tree = [INF] * size_tree
    lazy = [0] * size_tree

    build_tree(a_arr, seg_tree, 0, length - 1, 0)
    
    m = int(input())
    for i in range(m):
        temp_arr = list(map(int, input().split()))
        
        if len(temp_arr) == 2: 
            from_range = temp_arr[0]
            to_range  = temp_arr[1]
            
            if from_range > to_range: 
                min_range_1 = min_range_lazy(seg_tree, lazy, 0, length-1, from_range, length-1, 0)
                min_range_2 = min_range_lazy(seg_tree, lazy, 0, length-1, 0, to_range, 0)
                
                print(min(min_range_1, min_range_2))
            else: 
                print(min_range_lazy(seg_tree, lazy, 0, length-1, from_range, to_range, 0))
        else: 
            from_range = temp_arr[0]
            to_range  = temp_arr[1]
            delta = temp_arr[2]
            
            if from_range > to_range: 
                update_query_min_range_lazy(seg_tree, lazy, 0, length-1, from_range, length-1, delta, 0)
                update_query_min_range_lazy(seg_tree, lazy, 0, length-1, 0, to_range, delta, 0)
            else: 
                update_query_min_range_lazy(seg_tree, lazy, 0, length-1, from_range, to_range, delta, 0)\
            
        
    
    