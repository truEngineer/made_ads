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
    
    def cross_sgn(self, vec):
        if self.cross(vec) == 0:
            return 0
        else:
            return math.copysign(1, self.cross(vec))
    
    def contains(self, pnt: Point):
        # self: AB
        PA = Vector(pnt, self.point)
        PB = Vector(pnt,
                    Point(self.point.x + self.x,
                          self.point.y + self.y))
        if PA.cross(PB) == 0 and PA.dot(PB) <= 0:
            return True
        return False
    
    def crosses(self, vec):
        # self = AB
        A = self.point
        B = Point(A.x + self.x, A.y + self.y)
        # vec = CD
        C = vec.point
        D = Point(C.x + vec.x, C.y + vec.y)
        # signs of cross products
        sgn_ABxAC = self.cross_sgn(Vector(A, C))
        sgn_ABxAD = self.cross_sgn(Vector(A, D))
        if sgn_ABxAC * sgn_ABxAD <= 0:
            # signs of cross products
            sgn_CDxCA = vec.cross_sgn(Vector(C, A))
            sgn_CDxCB = vec.cross_sgn(Vector(C, B))
            if sgn_CDxCA * sgn_CDxCB <= 0:
                # check if vectors are lying on one line (all cross products == 0)
                if (sgn_ABxAC == 0 and sgn_ABxAD == 0) and (sgn_CDxCA == 0 and sgn_CDxCB == 0):
                    # check if segments on one line cross
                    if self.contains(C) or self.contains(D) or vec.contains(A) or vec.contains(B):
                        return True
                    else:
                        return False
                return True
        return False
 
 
Ax, Ay, Bx, By = map(int, input().split())
Cx, Cy, Dx, Dy = map(int, input().split())
AB = Vector(Point(Ax, Ay), Point(Bx, By))
CD = Vector(Point(Cx, Cy), Point(Dx, Dy))
if AB.crosses(CD):
    print("YES")
else:
    print("NO")
