import unittest
from zad8 import *


class TestRandomQueue(unittest.TestCase):

    def setUp(self):
        self.queue = RandomQueue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.insert(10)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        for i in range(15):
            self.queue.insert(i)

        self.assertTrue(self.queue.is_full())

    def test_insert(self):
        self.queue.insert(9)
        self.queue.insert(7)

        self.assertFalse(self.queue.is_empty())

        self.assertEqual(self.queue.remove(), 9)
        self.assertNotEqual(self.queue.remove(), 9)

    def test_remove(self):
        self.queue.insert(5)

        self.assertEqual(self.queue.remove(), 5)
        self.assertTrue(self.queue.is_empty())

        for i in range(5):
            self.queue.insert(i)

        self.assertTrue(self.queue.remove() in range(5))
        self.assertTrue(isinstance(self.queue.remove(), int))

    def test_insert_too_many(self):
        for i in range(15):
            self.queue.insert(i)
        with self.assertRaises(ValueError):
            self.queue.insert(11)

    def test_remove_too_many(self):
        with self.assertRaises(ValueError):
            self.queue.remove()

    def test_clear(self):
        for i in range(15):
            self.queue.insert(i)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()