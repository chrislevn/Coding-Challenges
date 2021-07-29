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


def binary_process(left, right, string, freq):
    """
    Check string in O(nlogn) complexity 
    
    Args: 
        left (int): starting index
        right (int): ending index
        string (str): check str
        freq (int): check frequency number 

    """
    global result
    
    while (left <= right): 
        mid = (right + left) // 2
        check = string[0:mid+1]
        prefix = [0] * len(check)
        KMP_preprocess(check, prefix)
        count = KMP_search(text, check, prefix)
        
        if count >= freq: 
            result = check
            left = mid + 1
        else: 
            right = mid - 1
                    
                
if __name__ == "__main__": 
    text = input()
    original = input()
    freq = int(input())
    
    count = ''
    result = ''
    
    binary_process(0, len(original)-1, original, freq)

    print(result if result != '' else 'IMPOSSIBLE')
        
            
    
    