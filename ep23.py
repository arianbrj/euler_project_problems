from math import sqrt

def factors_sum(n):
    s = 0
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            s += i
            if i != n // i :
                s += n // i
    return s 



def isAboundant(n):
    if  factors_sum(n) > n:
        return True

summation = 0


for i in range(1,28123):
    if i < 24:
        summation += i
        print(i)
    else:
        a,b = 0,-1
        flag = True
        possible_sums = list(range(0,i+1))
        # print(i,possible_sums)
        for j in range(len(possible_sums)//2 +1):
            # print(possible_sums[a],possible_sums[b])
            if isAboundant(possible_sums[a]) and isAboundant(possible_sums[b]):
                # print(possible_sums[a],possible_sums[b])
                flag = False
                break
            a += 1
            b -= 1
        if flag == True:
            summation += i
            print(i)
print(summation)