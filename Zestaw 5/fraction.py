# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. 
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
# Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.

import math
import unittest

def add_frac(frac1, frac2):        # frac1 + frac2
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]

    nwd = math.gcd(numerator, denominator)

    return [numerator/nwd, denominator/nwd]

def sub_frac(frac1, frac2):       # frac1 - frac2
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]

    nwd = math.gcd(numerator, denominator)

    return [numerator/nwd, denominator/nwd]

def mul_frac(frac1, frac2):       # frac1 * frac2
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]

    nwd = math.gcd(numerator, denominator)

    return [numerator/nwd, denominator/nwd]

def div_frac(frac1, frac2):        # frac1 / frac2
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]

    nwd = math.gcd(numerator, denominator)

    return [numerator/nwd, denominator/nwd]

def is_positive(frac):            # bool, czy dodatni
    if(frac[0]*frac[1] < 0):
        return False
    else:
        return True

def is_zero(frac):                 # bool, typu [0, x]
    if(frac[0] ==  0):
        return True
    else:
        return False

def cmp_frac(frac1, frac2):      # -1 | 0 | +1
    f1 = frac2float(frac1)
    f2 = frac2float(frac2)

    if(f1>f2):  # type: ignore
        return 1
    elif(f1 == f2):
        return 0
    elif(f2>f1): #type: ignore
        return -1

def frac2float(frac):           # konwersja do float
    float_value = float(frac[0] / frac[1])
    return float_value

f1 = [-1, 2]      # -1/2
f2 = [1, -2]      # -1/2 (niejednoznaczność)
f3 = [0, 1]       # zero
f4 = [0, 2]       # zero (niejednoznaczność)
f5 = [3, 1]       # 3
f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1,6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(f1 , f6) ,  [-3, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac([18,4] , [9,2]) ,  [1, 1])

    def test_is_positive(self):
        self.assertFalse(is_positive(f1))
        self.assertTrue(is_positive(f6))

    def test_is_zero(self):
        self.assertFalse(is_zero(f5))
        self.assertTrue(is_zero(f3))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(f3,f4), 0)
 
    def test_frac2float(self):
        self.assertEqual(frac2float(f1), -0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy