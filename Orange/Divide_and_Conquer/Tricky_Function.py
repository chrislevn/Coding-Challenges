import math, sys
sys.setrecursionlimit(int(1e5))

INF = 1e9 


class Point: 
    def __init__(self, x = 0, y = 0): 
        self.x = x 
        self.y = y 


def distance(p1, p2): 
    """
    Calculate distance by Euler formula
    
    Argr: 
        @p1: first point
        @p2: second point
    
    Return: 
        distance of the two points
    """
    x = p1.x - p2.x
    y = p1.y - p2.y 
    return (x * x + y * y)


def bruteForce(points, left, right):
    """
    Find minimum distance between 6 points 
    Args: 
        @points: list of points 
        @left: pairs of points on the left side
        @right: pairs of points on the right side
        
    Return: 
        The minimum distance
    
    """
    min_dist = INF
    for i in range(left, right): 
        for j in range(i+1, right): 
            min_dist = min(min_dist, distance(points[i], points[j]))
            
    return min_dist
    

def scripCloset(point_set, left, right, mid, dist_min): 
    """
    Combine left and right after division 
    Args: 
        @point_set: list of points 
        @left: set of points on the left
        @right: set of points on the right
        @mid: the middle point
        @dist_min: the parallel line to x-axis
        
    Return: 
        The minimum distance of combined left and right parts
    """
    point_mid = point_set[mid]
    splitted_points = []
    
    for i in range(left, right): 
        if abs(point_set[i].x - point_mid.x) <= dist_min: 
            splitted_points.append(point_set[i])
    
    splitted_points.sort(key=lambda p: p.y)
    smallest = dist_min
    l = len(splitted_points)
    
    for i in range(0, l): 
        for j in range(i+1, l): 
            if not (splitted_points[j].y - splitted_points[i].y)**2 < smallest:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)
                
    return smallest


def minimalDistance(point_set, left, right): 
    """
    Find the minimum distance in the point set 
    
    Args: 
        @point_set: list of points 
        @left: set of points on the left
        @right: set of points on the right
    
    Return: 
        Return the minimal distance
    """
    if right - left <= 3: 
        return bruteForce(point_set, left, right)
    mid = (left + right) // 2
    dist_left = minimalDistance(point_set, left, mid)
    dist_right = minimalDistance(point_set, mid+1, right)
    dist_min = min(dist_left, dist_right)
    
    return min(dist_min, scripCloset(point_set, left, right, mid, dist_min))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [0]
    for i in range(len(a)): 
        prefix.append(a[i] + prefix[-1])

    point_set = []

    for i in range(len(a)): 
        point_set.append(Point(prefix[i+1], i))

    result = minimalDistance(point_set, 0, n)
    print(result)
    
    