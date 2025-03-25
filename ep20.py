def factoreil(n):
    if n == 0:
        return 1
    else:
        return n * factoreil(n - 1)
    
hf = str(factoreil(100))

sum = 0
for number in hf:
    sum += int(number)

print(sum)

