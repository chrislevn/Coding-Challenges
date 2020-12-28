def areFriend(personA, personB): 
    for ch in personA: 
        if ch in personB: 
            return True
    return False


class Node: 
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id 

    # compare method 
    def __lt__(self, other):
        return self.dist <= other.dist 


if __name__ == "__main__":
    t = int(input())

    for i in range(t): 
        graph = [[] for i in range(25)]

        n, q = map(int, input().split())
        arr = list(map(str, input().split(' ')))

        for j in range(len(arr)): 
            for k in range(j+1, len(arr)): 
                if areFriend(arr[j], arr[k]): 
                    graph[j].append(k)
                    graph[k].append(j)

        for j in range(q): 
            x, y = map(int, input().split())

        print(graph)


