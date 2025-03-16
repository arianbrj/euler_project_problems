first , second = 1 ,1
s = 0

while first < 4*10**6:
	if first % 2 ==0:
		s += first
	# print(first)
	third = first + second
	first = second
	second = third

print(s)	

