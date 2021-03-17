def fib(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    cache[n] = fib(n - 1) + fib(n - 2)
    
    return cache[n]

print(fib(5))
print(fib(8))
print(fib(100))
