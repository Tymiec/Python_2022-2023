# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

lista1 = "97rp6 f7`34tr19"
lista2 = "kgjsfa'lirhy20933333333 "

print("Lista 1:", lista1)
print("Lista 2:", lista2,"\n")

zad_a = set(list(lista1)).intersection(lista2)
print(f"Lista wspólnych elementów", zad_a, "\n")

print(f"Zbiór bez powtórzeń elementów listy 1:", set(lista1), "\n")

print(f"Zbiór bez powtórzeń elementów listy 2:", set(lista2))