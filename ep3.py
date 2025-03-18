# largest prime factor of number : 600851475143
number = 600851475143


def isprime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    
    elif x != 2 and x % 2 == 0 :
        return False
    
    else:
        flag = True
        for i in range(3,int(x**.5)+1,2):
            if x % i == 0:
                flag = False
                break
        return flag
    
def factors(n):
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i * i != n:  # Avoid adding square root twice for perfect squares
                factors.append(n // i)
        i += 1
    return sorted(factors)

if __name__ == "__main__":
    big_number_factors = [j for j in factors(number) if isprime(j)]

    # [71, 839, 1471, 6857]
    print(max(big_number_factors))
    for i in range(50):
        if isprime(i):
            print(i)
