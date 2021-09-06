from math import ceil, log2
INF = 10**9 

class Bracket: 
    def __init__(self, match, open, close):
        """Create Bracket object

        Args: 
            match: number of successful pair
            open: number of open brackets
            close: number of close brackets
        
        """
        
        self.match = match
        self.open = open 
        self.close = close

    def __str__(self):
        return "Test Node {} - {} - {}".format(self.match, self.open, self.close)


def build_tree(a, seg_tree, left, right, index): 
    """Create segment tree
    
    Args: 
        a (list): list of initial values
        seg (tree): segment tree
        left (int): left index
        right (int): right index
        index (int): current index
    
    """
    
    if left == right: 
        if a[left] == "(": 
            seg_tree[index] = Bracket(0, 1, 0)
        elif a[left] == ")": 
            seg_tree[index] = Bracket(0, 0, 1)
        return 
    mid = (left + right) // 2
    build_tree(a, seg_tree, left, mid, 2 * index + 1)
    build_tree(a, seg_tree, mid + 1, right, 2 * index + 2)
    # seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]

    seg_tree[index] = Bracket(0, 0, 0)
    left_node = seg_tree[2 * index + 1]
    right_node = seg_tree[2 * index + 2]
    # print("Test left right", left, right)
    # print("Left", left_node)
    # print("Right", right_node)

    seg_tree[index].match = left_node.match + right_node.match
    open_single = left_node.open - left_node.match
    close_single = right_node.close - right_node.match
    seg_tree[index].match += min(open_single, close_single)
    seg_tree[index].open = left_node.open + right_node.open
    seg_tree[index].close = left_node.close + right_node.close


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


def update_query(seg_tree, a, left, right, index, pos, value): 
    """Update query 
    
    Args: 
        seg_tree (tree): segment tree 
        left (int): left index
        right (int): right index
        fr (int): starting position 
        to (int): ending position 
        index (int): current index 
        pos (int): current position 
        value (int): 1 for (, -1 for )
    
    """
    
    if pos < left or right < pos: 
        return 
    if pos == left and left == right: 
        if value == 1: 
            a[pos] = "("
            seg_tree[index] = Bracket(0, 1, 0)
        else: 
            a[pos] = ")"
            seg_tree[index] = Bracket(0, 0, 1)
        return 
    mid = (left + right) // 2
    if pos <= mid: 
        update_query(seg_tree, a, left, mid, 2 * index + 1, pos, value)
    else: # if pos > mid 
        update_query(seg_tree, a, mid+1, right, 2 * index + 2, pos, value)
    # seg_tree[index] = seg_tree[2 * index + 1] + seg_tree[2 * index + 2]  
    seg_tree[index] = Bracket(0, 0, 0)
    left_node = seg_tree[2 * index + 1]
    right_node = seg_tree[2 * index + 2]

    seg_tree[index].match = left_node.match + right_node.match
    open_single = left_node.open - left_node.match
    close_single = right_node.close - right_node.match
    seg_tree[index].match += min(open_single, close_single)
    seg_tree[index].open = left_node.open + right_node.open
    seg_tree[index].close = left_node.close + right_node.close


if __name__ == '__main__': 
    for test_case in range(10): 
        n_bracket = int(input())
        bracket_arr = list(input())

        n = len(bracket_arr)
        h = ceil(log2(n)) # log2: log base 2
        size_tree = 2 * (2**h) - 1
        seg_tree = [INF] * size_tree
        build_tree(bracket_arr, seg_tree, 0, n - 1, 0)

        print("Test {}:".format(test_case+1))

        m = int(input())
        for j in range(m): 
            k = int(input())
            if k == 0: 
                temp = seg_tree[0].match 
                # print("Test match", temp)

                if (temp == (n // 2)) and seg_tree[0].open == seg_tree[0].close: 
                    print("YES")
                else: 
                    print("NO")
            else: 
                if bracket_arr[k-1] == "(":
                    update_query(seg_tree, bracket_arr, 0, n-1, 0, k-1, -1)
                else: 
                    update_query(seg_tree, bracket_arr, 0, n-1, 0, k-1, 1)
                # print("Test", seg_tree[0].match, seg_tree[0].open, seg_tree[0].close)
