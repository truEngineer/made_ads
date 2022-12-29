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
        return Vector(Point(x=0, y=0),
                      Point(self.x + vec.x,
                            self.y + vec.y))
    
    def dot(self, vec):
        return self.x * vec.x + self.y * vec.y
    
    def cross(self, vec):
        return self.x * vec.y - self.y * vec.x
    
    def contains(self, pnt: Point):
        PA = Vector(pnt, self.point)
        PB = Vector(pnt,
                    Point(self.point.x + self.x,
                          self.point.y + self.y))
        if PA.cross(PB) == 0 and PA.dot(PB) <= 0:
            return True
        return False
    
 
Px, Py, Ax, Ay, Bx, By = map(int, input().split())
AB = Vector(Point(Ax, Ay), Point(Bx, By))
if AB.contains(Point(Px, Py)):
    print("YES")
else:
    print("NO")
