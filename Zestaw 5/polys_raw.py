# Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach. 
# Wielomian będzie reprezentowany przez listę swoich współczynników, 
# np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. 

# Napisać kod testujący moduł polys.

import unittest

def add_poly(poly1, poly2): pass        # poly1(x) + poly2(x)

def sub_poly(poly1, poly2): pass        # poly1(x) - poly2(x)

def mul_poly(poly1, poly2): pass        # poly1(x) * poly2(x)

def is_zero(poly): pass                 # bool, [0], [0,0], itp.

def eq_poly(poly1, poly2): pass        # bool, porównywanie poly1(x) == poly2(x)

def eval_poly(poly, x0): pass           # poly(x0), algorytm Hornera

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n): pass             # poly(x) ** n

def diff_poly(poly): pass               # pochodna wielomianu

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)



class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self): pass

    def test_mul_poly(self): pass

    def test_is_zero(self): pass

    def test_eq_poly(self): pass

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy