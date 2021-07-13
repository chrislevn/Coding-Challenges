def process_number(n): 
    output = list(map(int, str(n)))  
    return output

# def is_palindromic(string):  
    

if __name__ == "__main__": 
    t = int(input())

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    for i in range(t): 
        n = int(input())
        temp = process_number(n) 
        sum_of_str = sum(temp)

        letter = sum_of_str*(''.join([alphabet[x] for x in temp]))
        letter = letter[:sum_of_str]

        if letter == letter[::-1]: 
            print("YES")
        else: 
            print("NO")
        
