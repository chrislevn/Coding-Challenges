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
    
    
def KMPSearch(t, p, prefix): 
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
    
    while i < n: 
        if p[j] == t[i]: 
            i += 1
            j += 1
        if j == m: 
            print("Found pattern at index:", i - j)
            j = prefix[j - 1]
        elif i < n and p[j] != t[i]: 
            if j != 0: 
                j = prefix[j - 1]
            else: 
                i += 1


if __name__ == '__main__': 
    s = input()
    
    length = len(s)
    prefix = [0] * length
    KMP_preprocess(s, prefix)
    
    X1 = prefix[length - 1]
    X2 = prefix[X1 - 1]
    
    if len(s) == 1: 
        print("Just a legend")
        exit()
 
    if X1 > 0 and X1 in prefix[1:(length - 1)]: 
        print(s[:X1])
        exit()
    elif X2 > 0 and X2 in prefix[1:(length - 1)]:
        print(s[:X2])
        exit()
    else: 
        print("Just a legend")
