n = 100
s = 0
sq = 0
for i in range(1,n+1):
    s += i
    sq += i**2

s = s**2

print(s-sq)