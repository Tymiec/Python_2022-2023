# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. 
# Wskazówka: str.zfill().

import random

L_jednocyfrowa = random.sample(range(1, 10), 1)
L_dwucyfrowa = random.sample(range(10, 100), 1)
L_trzycyfrowa = random.sample(range(100, 1000), 1)

print("Wylosowana liczba jednocyfrowa:", L_jednocyfrowa)
print("Wylosowana liczba dwucyfrowa:", L_dwucyfrowa) 
print("Wylosowana liczba trzycyfrowa:", L_trzycyfrowa)
print("\n")

liczby = L_jednocyfrowa + L_dwucyfrowa + L_trzycyfrowa

# print(liczby)
dopelnione = []

for numbers in liczby:
    dopelnione.append(str(numbers).zfill(3))

print("Dopelnione zerami wylosowane liczby:", dopelnione)

