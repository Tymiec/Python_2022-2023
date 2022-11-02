# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie 
# (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
print(roman_to_int)

roman_to_int_2 = dict({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})
print(roman_to_int_2)

roman_to_int_pairs = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),('C', 100), ('D', 500), ('M', 1000)])
print(roman_to_int_pairs)