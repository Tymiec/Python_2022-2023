# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, 
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, 
# czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
# lista = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

def sum_sequento(lista):
    out = 0
    for x in lista:
        if(isinstance(x, (list, tuple))):
            out += sum_sequento(x)
        else:
            out += x
    return out

print(sum_sequento([[], [4], (1, 2), [3, 4], (5, 6, 7)]))