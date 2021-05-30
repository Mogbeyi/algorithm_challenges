'''
1, 2, 3, 5, 8, 13, 21, 34, 55
'''
def sum_even_fib(n):
    prev, curr = 1, 2
    even_sum = 0
    is_even = lambda x: x % 2 == 0

    while prev < n:
        prev, curr = curr, prev + curr
        
        if is_even(prev):
            even_sum += prev 

    return even_sum
    
print(sum_even_fib(4000000))
