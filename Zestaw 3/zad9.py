# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
# Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja
# spodziewany wynik [0,4,3,7,18].

lista = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

print([sum(i) for i in lista])