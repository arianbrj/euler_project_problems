def factoreil(n):
    if n <= 1:
        return 1
    p = 1
    for i in range(1,n+1):
        p *= i
    return p

def nth_number(n, l):
    if n > factoreil(l):
        return "Error! The number you entered cannot exist! Limit=%s" % factoreil(l)
    
    p = list(map(str, range(l)))  # Create a list of digits as strings
    number = ''
    n -= 1  # Convert to zero-based index
    while len(number) != l:
        step = factoreil(len(p) - 1)
        index = n // step  # Determine the index of the current digit
        number += p[index]  # Append the digit at the index to the result
        p.pop(index)  # Remove the used digit from the list
        n %= step  # Update n to the remainder for the next iteration
    return number

print(nth_number(10**6,10))