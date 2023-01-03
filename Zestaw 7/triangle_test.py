import unittest
from points import Point
from triangles import Triangle

class TestTriangle(unittest.TestCase):
    def test_init(self):
        # Test valid triangle
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(t1.pt1, Point(0, 0))
        self.assertEqual(t1.pt2, Point(1, 0))
        self.assertEqual(t1.pt3, Point(0, 1))

        # Test non-triangle
        with self.assertRaises(ValueError):
            t2 = Triangle(0, 0, 0, 0, 0, 0)

    def test_str(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(str(t1), "[(0, 0), (1, 0), (0, 1)]")

    def test_repr(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(repr(t1), "Triangle(0, 0, 1, 0, 0, 1)")

    def test_eq(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        t2 = Triangle(0, 0, 1, 0, 0, 1)
        t3 = Triangle(1, 0, 0, 1, 0, 0)
        self.assertTrue(t1 == t2)
        self.assertFalse(t1 != t3)

    def test_ne(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        t2 = Triangle(0, 0, 1, 0, 0, 1)
        t3 = Triangle(1, 0, 0, 1, 0, 0)
        self.assertFalse(t1 != t2)
        self.assertTrue(t1 == t3)

    def test_center(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(t1.center(), Point(1/3, 1/3))

    def test_area(self):
        self.assertEqual(Triangle(0, 0, 0, 3, 4, 0).area(), 6)

    def test_move(self):
        t1 = Triangle(0, 0, 1, 0, 0, 1)
        t1_moved = t1.move(1, 1)
        self.assertEqual(t1_moved, Triangle(1, 1, 2, 1, 1, 2))

    def test_make4(self):
        self.assertEqual(Triangle(0, 0, 0, 4, 2, 4).make4(), (
            Triangle(0, 0, 1.0, 2.0, 0.0, 2.0),
            Triangle(0, 4, 1.0, 4.0, 0.0, 2.0),
            Triangle(2, 4, 1.0, 2.0, 1.0, 4.0),
            Triangle(1.0, 4.0, 1.0, 2.0, 0.0, 2.0)))

if __name__ == '__main__':
    unittest.main()