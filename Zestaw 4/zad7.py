# Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, 
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), 
# która zwróci spłaszczoną listę wszystkich elementów sekwencji. 
# Wskazówka: 
# rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
# wykonać przez isinstance(item, (list, tuple)).

# seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]


def flatten(sequento):
    out = []
    for element in sequento:
        if isinstance(element, (list, tuple)):
            out += (flatten(element))
        else:
            out.append(element)
    return out

print(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))