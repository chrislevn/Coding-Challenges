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
                    
                        
def find_divisor(n): 
    """
    Find all divisor of a number
    
    Args: 
        n (int): input number
    
    Returns: 
        result (list): list of divisors of the number
    """
    i = 1
    result = []
    while i <= n: 
        if (n % i == 0): 
            result.append(i)
        i += 1
    return result


if __name__ == '__main__': 
    input_letter = input()
    while input_letter != '*': 
        length = len(input_letter)
        divisors = find_divisor(length)
        
        S = len(input_letter)
        
        prefix = [0] * len(input_letter)
        KMP_preprocess(input_letter, prefix)
        N = S * 1//(S - prefix[S-1])
        res = S - prefix[S - 1]
        
        if S % res == 0:         
            print(N)
        else: 
            print(1)
            
        input_letter = input()
        
        