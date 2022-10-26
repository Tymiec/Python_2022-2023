max = 30
n = 1
L = []
while n <= max:
    if n % 3 != 0:
        L.append(n)
    n = n+1

print(L)