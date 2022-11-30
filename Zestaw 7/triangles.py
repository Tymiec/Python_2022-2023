# W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami. 
# Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł triangles.
from points import Point
import math

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        l1 = self.pt1.distance(self.pt2)
        l2 = self.pt1.distance(self.pt3)
        l3 = self.pt2.distance(self.pt3)
        if l1 > l2 + l3:
            raise ValueError("Not a triangle")
        elif l2 > l1 + l3:
            raise ValueError("Not a triangle") 
        elif l3 > l1 + l2:
            raise ValueError("Not a triangle")

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

    def center(self):         # zwraca środek trójkąta
        triangle_x = (self.pt1.x, self.pt2.x, self.pt3.x)/3
        traingle_y = (self.pt1.y, self.pt2.y, self.pt3.y)/3
        return Point(triangle_x, traingle_y)

    def area(self):            # pole powierzchni
        v1 = self.pt1.distance(self.pt2)
        v2 = self.pt1.distance(self.pt3)
        v3 = self.pt2.distance(self.pt3)
        a = sum(v1,v2,v3)/2
        return math.sqrt(a * (a - v1) * (a - v2) * (a - v3))

    def move(self, x, y):      # przesunięcie o (x, y)
        vec = Point(x, y)
        self.pt1 += vec
        self.pt2 += vec
        self.pt3 += vec
        return self

    def make4(self):           # zwraca krotkę czterech mniejszych
        v1_v2 = Point((self.pt1.x + self.pt2.x)/2 , (self.pt1.y + self.pt2.y)/2)
        v2_v3 = Point((self.pt2.x + self.pt3.x)/2 , (self.pt2.y + self.pt3.y)/2)
        v3_v1 = Point((self.pt3.x + self.pt1.x)/2 , (self.pt3.y + self.pt1.y)/2)

        triangle_1 = Triangle(self.pt1.x , self.pt1.y , v1_v2.x , v1_v2.y , v3_v1.x , v3_v1.y)
        triangle_2 = Triangle(self.pt2.x , self.pt2.y , v1_v2.x , v1_v2.y , v2_v3.x , v2_v3.y)
        triangle_3 = Triangle(self.pt3.x , self.pt3.y , v2_v3.x , v2_v3.y , v3_v1.x , v3_v1.y)

        triangle_middle = Triangle(v1_v2.x , v1_v2.y , v2_v3.x , v2_v3.y , v3_v1.x , v3_v1.y)
        return (triangle_1 , triangle_2  , triangle_3 , triangle_middle)
#     A       po podziale    A
#    / \                    /1\
#   /   \                  +---+
#  /     \                /3\ /2\
# C-------B              C---+---B
