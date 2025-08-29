
import sys


import math

def largest_prime_factor(n):
    while n % 2 == 0:
        last_factor = 2
        n //= 2

    factor = 3
    last_factor = 2
    max_factor = math.isqrt(n) 

    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            last_factor = factor
            while n % factor == 0: 
                n //= factor
            max_factor = math.isqrt(n)
        factor += 2  

   
    if n > 1:
        last_factor = n

    return last_factor



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
    


