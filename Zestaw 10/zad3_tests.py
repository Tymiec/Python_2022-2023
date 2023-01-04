import unittest
from zad3 import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(6)
    
    def test_push(self):
        self.stack.push(6)
        self.stack.push(6)
        self.stack.push(6)
        self.stack.push(6)
        self.stack.push(6)
        self.stack.push(9)
        self.assertEqual(self.stack.size, 6)
        self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.count(), 2)

    def test_full_exception(self):
        stack = Stack(2)
        stack.push(2)
        stack.push(7)
        with self.assertRaises(ValueError):
            stack.push(2)
        stack = Stack(4)
        stack.push(2)
        stack.push(7)
        stack.push(5)
        stack.push(1)
        with self.assertRaises(ValueError):
            stack.push(4)

    def test_empty_exception(self):
        stack = Stack(10)
        with self.assertRaises(ValueError):
            stack.pop()

if __name__ == "__main__":
    unittest.main()