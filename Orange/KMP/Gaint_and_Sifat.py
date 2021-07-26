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
    
    Return: 
        result: number of times s occurs as 
                a substring in S after 
                removing all spaces from S.
    """
    
    n = len(t)
    m = len(p)
    i = j = 0
    result = 0
    
    while i < n: 
        if p[j] == t[i]: 
            i += 1
            j += 1
        if j == m: 
            result += 1
            j = prefix[j - 1]
        elif i < n and p[j] != t[i]: 
            if j != 0: 
                j = prefix[j - 1]
            else: 
                i += 1
    return result


def preprocess_string(input_string): 
    """ 
    Elimate spaces in string
    
    Args: 
        input_string (str): input string
    
    Return: 
        result (str): preprocessed string
    """
    result = input_string.replace(" ", "")
    return result


if __name__ == '__main__': 
    t = int(input())
    for i in range(t): 
        S = input()
        S = preprocess_string(S)
        
        s = input()
        s = preprocess_string(s)
        
        prefix = [0] * len(S)
        KMP_preprocess(S, prefix)
        final_result = KMP_search(S, s, prefix)
        
        print("Case {}: {}".format(i + 1, final_result))