def fib(n):
    global lookup
    if n == 0:
        return 0
    if n == 1:
        return 1
    if lookup[n] is not None: #checa se está em cache
        return lookup[n]
    lookup[n] = fib(n - 1) + fib(n - 2) #array auxiliar que atua como cache
    return lookup[n]


lookup = [None]*1000

print(fib(5))
