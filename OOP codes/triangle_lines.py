import math


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def distance(self):
        return self.l1 == self.l2 and self.l2 == self.l3

    def perimeter(self):
        return self.l1 + self.l2 + self.l3

    def area(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s*(s-self.l1)*(s-self.l2)*(s-self.l3))


t0 = Triangle((1, 1), (2, 3), (1, 1))
t1 = Triangle((1, 1), (1, 3), (4, 5))
print("Perimeter:", t1.perimeter())
print("area:", t1.area())
