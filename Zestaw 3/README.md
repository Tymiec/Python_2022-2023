# Język Python 
<!-- Język wonsz -->
> Autor: Tymiec
## Zestaw 3:

### Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

#### Zadanie 1

```python
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
```

> Podany kod jest poprawny składniowo, zbędne jest jednak w tym przypadku używanie średników do zakończenia linii.

```python
for i in "axby": if ord(i) < 100: print (i)
```

> Podany kod nie jest poprawny składniowo, w tym przypadku po dwukropkach następne instrukcje umieszczamy dopiero w następnej linijce

```python
for i in "axby": print (ord(i) if ord(i) < 100 else i)
```

> Podany kod jest porawny składniowo


#### Zadanie 2

Co jest złego w kodzie:
```python
L = [3, 5, 4] ; L = L.sort()
```
> Słaba przejrzystość, gdybyśmy zamiast średnika użyli entera, kod byłby czytelniejszy.

```python
x, y = 1, 2, 3
```

> Nie możemy przypisać do dwóch zmiennych, trzech wartości.

```python
X = 1, 2, 3 ; X[1] = 4
```

> Nie jesteśmy w stanie zmienić wartości w X które jest "Tuple" ponieważ wartości w tuple są *niezmienne**

```python
X = [1, 2, 3] ; X[3] = 4
```

> Nie możemy przypisać wartości do indeksu który nie istnieje

```python
X = "abc" ; X.append("d")
```

> metody .append używamy w przypadku list a nie zmiennych typu string

```python
L = list(map(pow, range(8)))
```

> Brak argumentów dla funkcji pow() przez co nie jest możliwe jej wykonanie

> Zaktualizowano 26.10.2022
