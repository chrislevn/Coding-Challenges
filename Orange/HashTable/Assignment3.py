TABLE_SIZE = 100000
PRIME = 33
hash_table = [-1 for i in range(TABLE_SIZE)]
curr_size = 0


def is_full(): 
    return curr_size == TABLE_SIZE


def hash1(key): 
    return key % TABLE_SIZE


def hash2(key): 
    return (PRIME - (key % PRIME))


def insert(key): 
    global curr_size
    if is_full(): 
        return 
    
    index1 = hash1(key)

    if hash_table[index1] != -1: 
        index2 = hash2(key)
        i = 1
        while True: 
            new_index = (index1 + i * index2) % TABLE_SIZE
            if hash_table[new_index] == -1: 
                hash_table[new_index] = key
                break
            i += 1
    else: 
        hash_table[index1] = key

    curr_size += 1


def search(key): 
    index1 = hash1(key)
    index2 = hash2(key)
    i = 0 
    while hash_table[(index1 + i * index2) % TABLE_SIZE] != key: 
        if hash_table[(index1 + i * index2) % TABLE_SIZE] == -1: 
            print("{} does not exist".format(key))
            return False, i
        i += 1
    print("{} found".format(key))
    return True, i


def delete(key): 
    condition = search(key)
    if condition[0]:
        index1 = hash1(key)
        index2 = hash2(key)
        i = condition[1]
        hash_table[(index1 + i * index2) % TABLE_SIZE] = -1
        print("{} deleted".format(key))


insert(12345678)
search(12345678)
delete(12345678)