def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def tail_fact(n, accum=1):
    if n == 1: 
        return accum  
    return tail_fact(n - 1, n * accum)

def main():
    print(tail_fact(5))

main()
