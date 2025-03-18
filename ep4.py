# largest palindrome with 3-digits multipication
def ispalindromeQM(x):
    x = str(x)
    flag = True
    a ,b=0,-1 
    for i in range(len(x)//2 + 1):
        if x[a] != x[b]:
            flag = False
            break
        a += 1
        b -= 1
    return flag


m = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if ispalindromeQM(i * j):
            if i*j > m:
                m = i*j
                ij = [i,j]            

print(m,ij)


