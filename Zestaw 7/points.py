# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. 
# Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). 

# Napisać kod testujący moduł points.
import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return(f"({self.x}, {self.y})")

    def __repr__(self):       # zwraca string "Point(x, y)"
        return (f"Point({self.x}, {self.y})")

    def __eq__(self, other):  # obsługa point1 == point2
        if not (isinstance(other,Point)):
            return False
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):        # długość wektora
        return math.sqrt(self.x**2 + self.y**2)
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def testStr(self):
        self.assertNotEqual(str(Point(3,4)), "(4, 3)")
        self.assertEqual(str(Point(7,8)), "(7, 8)")

    def testRepr(self):
        self.assertEqual(repr(Point(8,9)), "Point(8, 9)")
        self.assertNotEqual(repr(Point(5,4)), "Polnt(5, 4)")

    def test_eq(self):
        self.assertFalse(Point(2 , 3) == Point(3 , 3))
        self.assertTrue(Point(2 , 3) == Point(2 , 3))
        
    def testNe(self):
        self.assertNotEqual(Point(3, 6), Point(-3, 6))

    def testSum(self):
        self.assertEqual(Point(4, 3) + Point(1, 1), Point(5, 4))

    def testSub(self):
        self.assertEqual(Point(4, 3) - Point(1, 1), Point(3, 2))

    def testMul(self):
        self.assertEqual(Point(4, 3) * Point(2, -1), 5)

    def testCross(self):
        self.assertEqual(Point(-2, 6).cross(Point(3, 1)), -20)

    def testLen(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(5, 12).length(), 13)

if __name__ == '__main__':
    unittest.main()