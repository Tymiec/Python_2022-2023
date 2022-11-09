# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
# Lista jest modyfikowana w miejscu (in place). 
# Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie_iteracyjne(L, left, right):
    while right > left:
        L[left], L[right] = L[right], L[left]
        right -= 1
        left += 1

    return L

def odwracanie_rekurencyjne(L, left, right):
    if(right < left):
        return L
    
    L[left], L[right] = L[right], L[left]

    return odwracanie_rekurencyjne(L, left + 1, right - 1)

seq = [1,2,3,4,5,6,7]
id_1 = 0
id_2 = 3

print("\n")
print(seq)
print(f"Zamienianie iteracyjnie elementu L[{id_1}] z L[{id_2}]")
odwracanie_iteracyjne(seq, id_1, id_2)
print(seq)
print("\n")

seq = [0,2,4,8,10,12,16]
id_1 = 1
id_2 = 6

print(seq)
print(f"Zamienianie rekurencyjne elementu L[{id_1}] z L[{id_2}]")
odwracanie_rekurencyjne(seq, id_1, id_2)
print(seq)



