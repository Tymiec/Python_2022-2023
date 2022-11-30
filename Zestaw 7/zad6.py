# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
import itertools
import random

binary_iterator = itertools.cycle([0,1])
print("binary iterator")
for i in range (20):
    print(str(next(binary_iterator)))
news_iterator = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
print("news iterator")
for i in range (20):
    print(str(next(news_iterator)))
week_iterator = itertools.cycle([0,1,2,3,4,5,6])
print("week iterator")
for i in range (20):
    print(str(next(week_iterator)))

