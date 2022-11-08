# Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    for i in range(n+1):
        if n < 2:
            return n
        else:
            F_1=fibonacci(n-1)
            F_2=fibonacci(n-2)
            
            return (F_1 + F_2)

print(fibonacci(11))