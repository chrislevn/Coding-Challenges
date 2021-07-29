def KMP_preprocess(p, prefix): 
    """ 
    Preprocess function for KMP algoritm 
    
    Args: 
        p (str): pattern string
        prefix (list): output prefix
        
    """
    
    prefix[0] = 0
    m = len(p)
    Len = 0
    i = 1
        
    while i < m: 
        if p[i] == p[Len]: 
            Len += 1
            prefix[i] = Len
            i += 1
        else: 
            if Len != 0: 
                Len = prefix[Len - 1]
            else:
                prefix[i] = 0
                i += 1
    
    
def KMP_search(t, p, prefix): 
    """
    Search string in prefix
    
    Args: 
        t (str): input string 
        p (str): pattern string
        prefix (list): output prefix
        
    Returns: 
        count (int): number of time p in t
    """
    
    n = len(t)
    m = len(p)
    i = j = 0
    
    count = 0

    while i < n: 
        if p[j] == t[i]: 
            i += 1
            j += 1
        if j == m: 
            count += 1
            j = prefix[j - 1]
        elif i < n and p[j] != t[i]: 
            if j != 0: 
                j = prefix[j - 1]
            else: 
                i += 1
    return count
                    
def process_array(input_arr): 
    """
    Process array based on the elements' previous number
    
    Args: 
        input_array (list): input array
    
    Returns: 
        result_arr (list): processed array
        
    """
    result_arr = []
    for i in range(1, len(input_arr)): 
        result_arr.append(input_arr[i] - input_arr[i-1])
    return result_arr

if __name__ == '__main__': 
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if w == 1: 
        print(n)
        exit()
    
    a_temp = process_array(a)
    b_temp = process_array(b)
        
    prefix = [0] * len(b_temp)
    print(b_temp)
    
    KMP_preprocess(b_temp, prefix)
    print(prefix)

    print(KMP_search(a_temp,  b_temp, prefix))
    
