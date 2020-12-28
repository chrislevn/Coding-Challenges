import queue 

def topological_sort(graph, result): 
    indegree = [0] * (V)
    zero_indegree = queue.PriorityQueue()
    for u in range(V): 
        for v in graph[u]: 
            indegree[v] += 1
    
    for i in range(V): 
        if indegree[i] == 0: 
            zero_indegree.put(i)
    
    while not zero_indegree.empty(): 
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]: 
            indegree[v] -= 1
            if indegree[v] == 0: 
                zero_indegree.put(v)

    for i in range(V): 
        if indegree[i] != 0: 
            return False

    return True


def convertToNum(string): 
    res = []
    list_string = list(string)
    for char in list_string: 
        res.append(ord(char) - ord('a'))
    return res 

def helper(arr_1, arr_2): 
    pointer = 0

    while pointer < len(arr_1) and pointer < len(arr_2): 
        if arr_1[pointer] < arr_2[pointer]: 
            return arr_1[pointer], arr_2[pointer]
        elif arr_1[pointer] > arr_2[pointer]: 
            return arr_1[pointer], arr_2[pointer]
        else: 
            pointer += 1
    
    if len(arr_1) > len(arr_2): 
        print("Impossible")
        exit(0)
    else: 
        return None, None


if __name__ == "__main__": 
    n = int(input())

    input_arr = []
    for i in range(n): 
        letter = input()
        input_arr.append(convertToNum(letter))
    
    V = 26 
    E = (n*(n+1)) // 2

    graph = [[] for i in range(V+5)]
    result = []

    for i in range(n): 
        for j in range(i+1, n): 
            u, v = helper(input_arr[i], input_arr[j])
            if u is not None and v is not None: 
                graph[u].append(v)

    if (topological_sort(graph, result)): 
        for i in range(V): 
            print(chr(result[i] + ord('a')), end = '')
        
    else: 
        print('Impossible')