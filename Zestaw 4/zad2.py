# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
# które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, 
# tylko korzystać z argumentów.

def make_ruler(dlugosc):
    print("Linijka o długości:", dlugosc,"\n")
    podzialka = "|"
    mianownik = "0"

    for i in range(1, dlugosc + 1):
        podzialka += "....|"
        mianownik += str(i).rjust(5)

    linijka = podzialka + "\n" + mianownik
    return linijka

def make_grid(row, col):
    print(f"\nSiatka o wymiarach  {row} x {col}")
    sep = "\n" + "+---"*col + "+\n"
    return sep + ("|   "*col + "|" + sep)*row

print(make_ruler(10))
print(make_grid(5,5))

