from math import sqrt

def find_largest_prime_factor(n):
    start_range = (n // 2) + 1

    for num in range(start_range, 2, -1):
        if n % num == 0 and is_prime(num):
            return num

def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime(13195))
