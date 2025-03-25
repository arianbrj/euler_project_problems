from math import sqrt

def d(n):
    factors = set()
    factors.add(1)
    # factors.add(n)
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return sum(list(sorted(factors)))


ds = set()

for a in range(10000):
    b = d(a)
    db = d(b)
    if b == b and db == a and a != b:
        ds.add(a)
        ds.add(b)

print(sum(list(ds)))
        
