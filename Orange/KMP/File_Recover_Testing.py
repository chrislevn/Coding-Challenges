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
    input_value = input().split(" ")
    while input_value[0] != '-1': 
        prefix_value = input_value[1]
        K = int(input_value[0])

        prefix = [0] * len(prefix_value)
        KMP_preprocess(prefix_value, prefix)

        overlap = prefix[len(prefix_value) - 1]
        len_string_added = len(prefix_value) - overlap
        num_appearance = (K - len(prefix_value))// len_string_added + 1

        if num_appearance > 0:
            print(num_appearance)
        else: 
            print(0)
        input_value = input().split(" ")