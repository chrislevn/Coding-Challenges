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
    
#########

from math import ceil, log2
INF = 10**9 


def min_range(seg_tree, left, right, fr, to, index): 
    """
    Find min values of range 
    
    Args: 
        seg_tree (tree): segment tree 
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position 
        index (int): current index 
        
    Returns: 
        minimum value of a range
    
    """
    
    if fr <= left and right <= to: 
        return seg_tree[index]
    if fr > right or to < left: 
        return INF 
    
    mid = (left + right) // 2
    a = min_range(seg_tree, left, mid, fr, to, 2 * index + 1)
    b = min_range(seg_tree, mid + 1, right, fr, to, 2 * index + 2)
    return min(a, b)


if __name__ == '__main__': 
    a = [5, -7, 9, 0, -2, 8, 3, 6, 4, 1]
    n = len(a)
    h = ceil(log2(n)) # log2: log base 2
    size_tree = 2 * (2**h) - 1
    seg_tree = [INF] * size_tree
    build_tree(a, seg_tree, 0, n - 1, 0)
    from_range = 2
    to_range = 7
    
    min_value = min_range(seg_tree, 0, n-1, from_range, to_range, 0)
    print(min_value)
    
#######

from math import ceil, log2
INF = 10**9 


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
    return sum_range(seg_tree, left, mid, fr, to, 2 * index + 1) + \
        sum_range(seg_tree, mid + 1, right, fr, to, 2 * index + 2)


########

from math import ceil, log2
INF = 10**9 


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
    
    
if __name__ == '__main__': 
    a = [5, -7, 9, 0, -2, 8, 3, 6, 4, 1]
    n = len(a)
    h = ceil(log2(n)) # log2: log base 2
    size_tree = 2 * (2**h) - 1
    seg_tree = [INF] * size_tree
    build_tree(a, seg_tree, 0, n - 1, 0)
    from_range = 2
    to_range = 7
    min_value = min_range(seg_tree, 0, n-1, from_range, to_range, 0)
    print("Before update")
    print("Range minimum query:", min_value)
    
    # position update 
    pos = 4
    # value update
    value = 9 
    
    update_query(seg_tree, a, 0, n - 1, 0, pos, value)
    min_value = min_range(seg_tree, 0, n - 1, from_range, to_range, 0)
    print("After update")
    print("Range minimum query:", min_value)
    
    
#########
from math import ceil, log2
INF = 10**9 
lazy = [0] * size_tree


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
    if fr >= left and right <= to: 
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
    
    
####### 

lazy = [0] * size_tree


def update_query_sum_query_lazy(seg_tree, lazy, left, right, fr, to, delta, index): 
    """
    Update query with sum and lazy segment tree
    
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
        seg_tree[index] += lazy[index] * (right - left + 1)
        if left != right: 
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0 
        
    # no overlap condition 
    if fr > right or to < left: 
        return
    
    #total overlap condition 
    if fr <= left and right <= to: 
        seg_tree[index] += delta * (right - left + 1)
        if left != right: 
            lazy[2 * index + 1] += delta
            lazy[2 * index + 2] += delta
        return 
    
    #otherwise partial overlap so look both left and right 
    mid = (left + right) // 2
    update_query_min_range_lazy(seg_tree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    update_query_min_range_lazy(seg_tree, lazy, mid + 1, right, fr, to, delta, 2 * index + 2)
    seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]
        
                     
lazy = [0] * size_tree

def sum_query_lazy(seg_tree, lazy, left, right, fr, to, index): 
    """
    Find sum of a segment using lazy segment tree
    
    Args: 
        seg_tree (tree): segment tree
        lazy (tree): lazy segment tree
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position
        index (int): current index
        
    """
    
    if left > right: 
        return INF
    if lazy[index] != 0: 
        seg_tree[index] += lazy[index] * (right - left + 1)
        if left != right: # not a leaf node
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    
    # no overlap
    if fr > right or to > left: 
        return 0
    
    # total overlap
    if fr <= left and to >= right: 
        return seg_tree[index]
    
    #partal overlap 
    mid = (left + right) // 2
    return sum_query_lazy(seg_tree, lazy, mid + 1, right, fr, to, 2 * index + 2) + \
        sum_query_lazy(seg_tree, lazy, left, mid, fr, to, 2 * index + 1)


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