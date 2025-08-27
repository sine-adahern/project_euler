import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    a = 0
    b = 1
    nex = b  
    count = 1
    numbers = 0

    while nex <= n:
       
        count += 1
        a, b = b, nex
        nex = a + b
        if (nex % 2 ==0) and (nex <= 100) :
            print(nex)
            numbers = numbers + nex
    print(numbers)
