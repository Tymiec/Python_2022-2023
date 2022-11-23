# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. 
# Prostokąt jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego. 

# Napisać kod testujący moduł rectangles.

from points import Point #type: ignore

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):       # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):       # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'

    def __eq__(self, other):   # obsługa rect1 == rect2
        if(self.pt1 == other.pt1 and self.pt2 == other.pt2):
            return 1
        return 0

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):      # zwraca środek prostokąta
            return Point(((self.pt1 + self.pt2).x)/ 2, ((self.pt1 + self.pt2).y)/ 2)

    def area(self):         # pole powierzchni
        return ((abs(self.pt2.x - self.pt1.x)) * (abs(self.pt2.y - self.pt1.y)))
    def move(self, x, y):    # przesunięcie o (x, y)
        moved = Point(x, y)
        self.pt1 = self.pt1 + moved
        self.pt2 = self.pt2 + moved

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def testStr(self):
        self.assertEqual(str(Rectangle(3, 4, 6, 6)), "[(3, 4), (6, 6)]")

    def testRepr(self):
        self.assertEqual(repr(Rectangle(3, 4, 6, 6)), "Rectangle[(3, 4), (6, 6)]")

    def testEq(self):
        self.assertEqual(Rectangle(3, 4, 6, 6), Rectangle(3, 4, 6, 6))

    def testNe(self):
        self.assertNotEqual(Rectangle(3, 4, 6, 6), Rectangle(3, 4, 6, 7))

    def testCent(self):
        self.assertEqual(Rectangle(3, 4, 6, 6).center(), Point(4.5, 5))

    def testArea(self):
        self.assertEqual(Rectangle(3, 4, 6, 6).area(), 6)

    def testMove(self):
        rec = Rectangle(3, 4, 6, 6)
        rec.move(10, 10)
        self.assertEqual(rec, Rectangle(13, 14, 16, 16))

if __name__ == '__main__':
    unittest.main()
