# find summation of all primes < 2*10**6
# we use isprime function from ep3 file that we wrote before...
from ep3 import isprime

s = 2
for i in range(3,2*10**6 + 1,2):
    if isprime(i):
        s += i

print(s)
