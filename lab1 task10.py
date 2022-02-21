import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):  # ==
        return self.x is other.x and self.y is other.y

    def __ne__(self, other):  # !=
        return self.x is not other.x or self.y is not other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        import inspect
        if isinstance(other, Point):
            return((math.sqrt(self.x ** 2 + self.y ** 2) * math.sqrt(other.x ** 2 + other.y ** 2)))
        else:
            return Point(self.x * other, self.y * other)


    def len(self):
        return (math.sqrt(self.x ** 2 + self.y ** 2))

    def abs(self):
        return (math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return f'Point: {self.x}, {self.y}, point\'s length = {self.len()}'


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point()
print(p1==p2)
print(p1!=p2)
p3=p1+p2
print(p3)
print(p1-p2)
p3+=p1
print(p3)
p3-=p2
print(p3)
print(p1*p2)
p3 = p1*5
print(p3)
print(p1.len())
print(p1.abs())
