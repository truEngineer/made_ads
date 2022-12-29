import math
 
 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
 
class Vector():
    def __init__(self, point_1: Point, point_2: Point):
        self.point = point_1
        self.x = point_2.x - point_1.x
        self.y = point_2.y - point_1.y
        
    def add(self, vec):
        '''
        Returns the sum of two vectors: `self` and `vec`
        '''
        return Vector(Point(x=0, y=0),
                      Point(self.x + vec.x,
                            self.y + vec.y))
    
    def dot(self, vec):
        '''
        Dot product of vectors `self` and `vec`
        '''
        return self.x * vec.x + self.y * vec.y
    
    def cross(self, vec):
        '''
        Cross product of vectors `self` and `vec`
        '''
        return self.x * vec.y - self.y * vec.x
 
 
class Polygon():
    def __init__(self, verts):
        self.__n = len(verts)
        self.__verts = verts  # list of verts: list[Point]
 
    def square(self):
        '''
        Returns the square of the Polygon
        '''
        square = 0
        # select the point:
        x = 0
        y = 0
        for vert in self.__verts:
            x += vert.x
            y += vert.y
        pnt = Point(x / self.__n, y / self.__n)
        
        for ind, vert in enumerate(self.__verts):
            vec_1 = Vector(pnt, vert)  # vec to this vert
            if ind == self.__n - 1:
                vert2 = self.__verts[0]
            else:
                vert2 = self.__verts[ind + 1]
            vec_2 = Vector(pnt, vert2)  # vec to next vert
            square += vec_1.cross(vec_2)
        return abs(square) / 2
 
 
n = int(input())
verts = []
for _ in range(n):
    x, y = map(int, input().split())
    verts.append(Point(x, y))
poly = Polygon(verts)
 
print(poly.square())
