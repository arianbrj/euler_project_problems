# for this problem we're gonna use Optimized Brute Force algorithm!!
from math import sqrt

def triangular(n):
    return int(n * (n+1) / 2)

def find_factors(n):
    factors = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return sorted(factors)

# print(find_factors(1938472))

n = 1
x = triangular(n)
l = len(find_factors(x))
while l < 500:
    n += 1
    x = triangular(n)
    l = len(find_factors(x))

print(n,x,l)
