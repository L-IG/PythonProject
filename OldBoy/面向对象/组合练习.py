from math import pi

class circle():
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r **2 * pi
    def perimter(self):
        return 2 * pi * self.r


class Ring():
    def __init__(self,R,r):
        self.outside_c = circle(R)
        self.inside_c = circle(r)

    def area(self):
        return self.outside_c.area() - self.inside_c.area()


    def perimeter(self):
        return self.outside_c.perimter() + self.inside_c.perimter()

ring = Ring(20,10)