# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr 
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). 
# Należy zbudować pełny string, a potem go wypisać.

print("Wprowadz długość linijki:")
dlugosc = int(input())

print("Linijka o długości:", dlugosc,"\n")

podzialka = "|"
mianownik = "0"
for i in range(1, dlugosc + 1):
    podzialka += "....|"
    mianownik += str(i).rjust(5)

linijka = podzialka + "\n" + mianownik
print(linijka)