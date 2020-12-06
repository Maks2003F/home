def sum_fib(K):
    a = 1  
    b = 0 
    c = 0
    while a < K:
        c += a
        a,b = a + b, a
        return c
print(sum_fib(2))