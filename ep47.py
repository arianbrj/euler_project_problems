def isprime(x):
    if x <= 1 :
        return False
    elif x == 2 :
        return True
    elif (x != 2 and x % 2 == 0):
        return False
    else:
        flag = True
        for i in range(3,int(x**0.5)+1,2):
            if x % i == 0:
                flag = False
                break
        return flag


def factors(n):
    factors = []
    q = n
    for i in range(1,q+1):
        if n % i ==0 and isprime(i):
            factors += [i]
            q = n//i
    return factors


n = 134043
while True:
    if len(factors(n)) ==4 and len(factors(n+1)) ==4 and len(factors(n+2)) ==4 and len(factors(n+3)) ==4:
        print(n)
        break
    n += 1

print(n)
print(factors(n))
print(factors(n+1))
print(factors(n+2))
print(factors(n+3))
