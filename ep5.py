import ep3 
# in order to use isprime function
# ms = []
def small_multiplication(b):
    a,b,ms,p =2,b+1,[],1 
    for i in range(a,b):
        if ep3.isprime(i):
            c = 1
            while i ** c <= b:
                q = i**(c)
                # print(q,c,i)
                c += 1
            if q in ms:
                continue
            else:
                p *= q
                ms += [q]
    return p ,ms

# print(small_multiplication(100))

