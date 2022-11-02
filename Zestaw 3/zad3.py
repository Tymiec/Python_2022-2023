# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
max = 30
n = 1
L = []
while n <= max:
    if n % 3 != 0:
        L.append(n)
    n = n+1

print(L)