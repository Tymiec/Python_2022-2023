# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    out = 1
    for i in range(1, n+1):
        # print(f"Silnia: {out} x {i}")
        out = out * i

    return out

print(factorial(5)) 
        