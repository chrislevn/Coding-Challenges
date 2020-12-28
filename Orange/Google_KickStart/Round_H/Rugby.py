from collections import deque

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  
        self.dist = dist 


def BFS(graph, source, destination): 
    if graph[source.x][source.y] != 1 or graph[destination.x][destination.y] != 1:
        return -1

    visited = [[False for i in range(505)] for j in range(505)]
    visited[source.x][source.y] = True

    q = deque()

    s = queueNode(source, 0)
    q.append(s)

    while q:
        curr = q.popleft() 

        pt = curr.pt
        if pt.x == destination.x and pt.y == destination.y:
            return curr.dist
         
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
             
            if graph[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col), curr.dist+1)
                q.append(Adjcell)
     
    return -1


if __name__ == "__main__":
    t = int(input())
    graph = [[1] * 505] * 505

    for i in range(t): 
        n = int(input())
        
        dist = 10e9

        points = []
        for j in range(n): 
            x, y = map(int, input().split())
            points.append((x, y))

        length_points = len(points)
        result = 10e9
        

        for j in range(length_points): 
            remain_left = 0 - j 
            remain_right = length_points - j
            temp = 0
            
            for k in range(remain_left, remain_right): 
                x_des = points[j][0] + k
                if x_des != points[j][0] or k != j: 
                    y_des =  points[j][1]
                    
                    source = Point(points[k][0], points[k][1])
                    destination = Point(x_des, y_des)      

                    dist = BFS(graph, source, destination)
                    temp += dist
            
            if result > temp:
                result = temp 

        print("Case #{}: {}".format(i+1, result))

