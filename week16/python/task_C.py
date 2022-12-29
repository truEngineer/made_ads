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
    
    def angle(self, vec):
        '''
        Calculate the angle between vectors `self` and `vec`
        '''
        return math.atan2(self.cross(vec), self.dot(vec))
    
    def contains(self, pnt: Point):
        '''
        Check if the point `pnt` belongs to the vector `self`
        '''
        # self: AB
        PA = Vector(pnt, self.point)
        PB = Vector(pnt,
                    Point(self.point.x + self.x,
                          self.point.y + self.y))
        if PA.cross(PB) == 0 and PA.dot(PB) <= 0:
            return True
        return False
 
 
class Polygon():
    def __init__(self, verts):
        self.__n = len(verts)
        self.__verts = verts  # list of verts: list[Point]
 
    def contains(self, pnt):
        '''
        Check if the point `pnt` is inside the Polygon
        '''
        angle = 0
        for ind, vert in enumerate(self.__verts):
            vec_1 = Vector(pnt, vert)  # vec to this vert
            if ind == self.__n - 1:
                vert2 = self.__verts[0]
            else:
                vert2 = self.__verts[ind + 1]
            vec_2 = Vector(pnt, vert2)  # vec to next vert
            angle += vec_1.angle(vec_2)
            # check if point is lying on a rib
            if Vector(vert, vert2).contains(pnt):
                return True
        if math.isclose(abs(angle), 2 * math.pi):
            return True
        else:
            return False
 
 
n, Ox, Oy = map(int, input().split())
O = Point(Ox, Oy)
verts = []
for _ in range(n):
    x, y = map(int, input().split())
    verts.append(Point(x, y))
poly = Polygon(verts)
 
if poly.contains(O):
    print("YES")
else:
    print("NO")
