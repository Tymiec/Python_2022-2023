# W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami. 
# Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł triangles.
from points import Point
import math
import statistics

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
                    raise ValueError("The points are collinear")

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return (f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]")
    
    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return (f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})")
    
    def __eq__(self, other):   # obsługa tr1 == tr2
        triangle_1 = {self.pt1, self.pt2, self.pt3}
        traingle_2 = {other.pt1, other.pt2, other.pt3}
        if triangle_1 == traingle_2:
            return True
        return False

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
        x_coordinates = (self.pt1.x, self.pt2.x, self.pt3.x)
        y_coordinates = (self.pt1.y, self.pt2.y, self.pt3.y)
        x_center = statistics.mean(x_coordinates)
        y_center = statistics.mean(y_coordinates)
        return Point(x_center, y_center)

    def area(self):
        l1 = self.pt1.distance(self.pt2)
        l2 = self.pt1.distance(self.pt3)
        l3 = self.pt2.distance(self.pt3)
        p = (l1 + l2 + l3)/2
        return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))

    def move(self, x, y):      # przesunięcie o (x, y)
        vec = Point(x, y)
        self.pt1 += vec
        self.pt2 += vec
        self.pt3 += vec
        return self

    def make4(self):           # zwraca krotkę czterech mniejszych
        point12 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        point23 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        point13 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        return (Triangle(self.pt1.x, self.pt1.y, point13.x, point13.y, point12.x, point12.y),
                Triangle(self.pt2.x, self.pt2.y, point23.x, point23.y, point12.x, point12.y),
                Triangle(self.pt3.x, self.pt3.y, point13.x, point13.y, point23.x, point23.y),
                Triangle(point23.x, point23.y, point13.x, point13.y, point12.x, point12.y))
#     A       po podziale    A
#    / \                    /1\
#   /   \                  +---+
#  /     \                /3\ /2\
# C-------B              C---+---B


