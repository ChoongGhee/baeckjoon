import math

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int((math.sqrt(n)))+1, 2):
            if n % i == 0:
                return False
        return True

Z = int(input())

for z in range(Z):
    T = int(input())
        
    for i in range(T//2, 1, -1):
        
        if is_prime(i) and is_prime(T-i):
            print(i, T-i)
            break