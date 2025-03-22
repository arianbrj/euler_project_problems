def chain_builder(n):
    x = n
    c = 1
    while n != 1:
        if n % 2 ==0:
            n = n / 2
            c += 1
        else:
            n = 3*n +1
            c += 1
    return x,c

# print(chain_builder(13))  
max_chain = 0
for i in range(1*10**6,1,-1):
    cb = chain_builder(i)
    if cb[1] > max_chain:
        max_chain = cb[1]
        m = cb[0]

print(m,max_chain)