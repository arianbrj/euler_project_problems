import ep3



c = 1
n = 0 
limit = 10001
while n<limit:
    if ep3.isprime(c):
        n += 1
        print(c,n)
         
    c += 1
    
