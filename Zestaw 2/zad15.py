# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

import random

L = random.sample(range(0, 9), 5)
print(L)

print(''.join(str(num) for num in L))
