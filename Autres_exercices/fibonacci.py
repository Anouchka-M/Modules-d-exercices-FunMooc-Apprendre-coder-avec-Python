def fibo(n):
    """calcule le n-ième nombre de Fibonacci, avec : n de type int et
    fibo(0) valant 0
    fibo(1) valant 1 et
    fibo(n+1) valant fibo(n-1) + fibo(n)"""
    if n < 0 : # fibo(n) retourne None
        res = None
    else:
        res = 0
        suivant = 1
        for _ in range(n): # calcule n fois le nombre de Fibonacci suivant
            res, suivant = suivant, res + suivant
    return res

for i in range(100):
    print(fibo(i))

