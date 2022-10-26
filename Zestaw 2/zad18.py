# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

import random

L = random.randint(0, 1000000000000000000)
print("Losowo wygenerowana duża liczba całkowita:\n", L, "\n")
liczba_zer = str(L).count('0')
print("W losowo wygenerowanej liczba zero występuje tyle razy:\n", liczba_zer)