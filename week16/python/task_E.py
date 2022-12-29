import math
 
 
MAX = 1e9
 
 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x == other.x and self.y == other.y)
        else:
            return False
 
 
class Vector():
    def __init__(self, point_1: Point, point_2: Point):
        self.point = point_1
        self.x = point_2.x - point_1.x
        self.y = point_2.y - point_1.y
        self.len = math.sqrt(self.x ** 2 + self.y ** 2)
        
    def add(self, vec):
        '''
        Returns the sum of two vectors: `self` and `vec`
        '''
        return Vector(Point(x=0, y=0),
                      Point(self.x + vec.x,
                            self.y + vec.y))
    
    def polar_angle(self):
        '''
        Calculate the polar angle (from 0 to 2pi) for the vector (`self`)
        '''
        vec_x = Vector(Point(0, 0), Point(1, 0))
        polar_angle = math.atan2(vec_x.cross(self), vec_x.dot(self))
        if polar_angle < 0:
            return polar_angle + 2 * math.pi
        return polar_angle
    
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
        Returns a square of the Polygon
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
    
    def perimeter(self):
        '''
        Returns a perimeter of the Polygon
        '''
        perimeter = 0
        for ind, vert in enumerate(self.__verts):
            if ind == self.__n - 1:
                vert_next = self.__verts[0]
            else:
                vert_next = self.__verts[ind + 1]
            perimeter += Vector(vert, vert_next).len
        return perimeter
 
 
def graham(pnts):
    '''
    Returns minimal convex hull (Polygon) for `pnts`: list[Points]
    '''
    pnts = list(set(pnts))  # remove same points!
    min_y = MAX
    min_x = MAX
    ind_0 = None
    # find the leftest and the lowest point
    for ind, pnt in enumerate(pnts):
        if pnt.y < min_y:
            min_y = pnt.y
            min_x = pnt.x
            # save index of the leftest and the lowes point
            ind_0 = ind
        if pnt.y == min_y:
            if pnt.x < min_x:
                min_x = pnt.x
                # save index of the leftest and the lowes point
                ind_0 = ind
    pnt_0 = pnts[ind_0]
    conv_hull = [pnt_0]
    pnts.pop(ind_0)
        
    # calculate angles from p0 to other points
    angles = []
    for pnt in pnts:
        angles.append(Vector(pnt_0, pnt).polar_angle())
    # sorting by angle
    index = list(range(len(angles)))
    index.sort(key=angles.__getitem__)
    angles[:] = [angles[i] for i in index]
    pnts[:] = [pnts[i] for i in index]
    conv_hull.append(pnts.pop(0))  # now conv_hull contains first two points
    
    while len(pnts):
        new_pnt = pnts.pop(0)
        angle_last = Vector(conv_hull[-2], conv_hull[-1]).polar_angle()
        angle_new = Vector(conv_hull[-1], new_pnt).polar_angle()
        while angle_new < angle_last or math.isclose(angle_new, angle_last):
            # delete points from conv_hull while not the left turn
            conv_hull.pop()
            if math.isclose(angle_new, angle_last):  # on the same line
                break
            angle_last = Vector(conv_hull[-2], conv_hull[-1]).polar_angle()
            angle_new = Vector(conv_hull[-1], new_pnt).polar_angle()
        conv_hull.append(new_pnt)
    return Polygon(conv_hull)
 
 
n_pnts = int(input())
all_pnts = []
for _ in range(n_pnts):
    x, y = map(int, input().split())
    all_pnts.append(Point(x, y))
poly = graham(all_pnts)
print(poly.perimeter())
