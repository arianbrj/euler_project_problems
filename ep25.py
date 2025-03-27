def fib(n):
    first ,second = 1,1
    for i in range(1,n):
        third = first + second
        first = second
        second = third
    return first


for i in range(1,13):
    print(i,fib(i))



c = 0
while len(str(fib(c))) != 10**3:
    c += 1

print(c)