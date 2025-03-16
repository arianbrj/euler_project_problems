##### arian

# 0.1234567891011121314151617181920.....
# 400 - 9*1 - 90*2 -900*3 
def ranGSaz(d):
    n = 1
    w = 1
    while d > 0:
        d1 = d
        d -= w*n*9
        n *= 10 
        w += 1
    n = 10
    w -= 1
    start = list(str((n**(w-1)) + (d1//w)))
    
    return int(start[d1%w])
    
    


# ...5354555657....
# print(ranGSaz(100))

n = 10
p = 1
for i in range(7):
    print(ranGSaz(n**i))
    p *= ranGSaz(n**i)
    

print(p)

#100101102013104105
ranGSaz(1905)


##### grok
def ranGSaz(d):
    if d <= 0:
        return 0
    
    total_digits = 0
    digits_per_number = 1
    start_number = 1
    
    # محاسبه گروه حاوی رقم d
    while True:
        numbers_in_group = 9 * (10 ** (digits_per_number - 1))
        group_digits = numbers_in_group * digits_per_number
        
        if total_digits + group_digits >= d:
            break
            
        total_digits += group_digits
        start_number *= 10
        digits_per_number += 1
    
    # محاسبه آفست در گروه
    offset = d - total_digits - 1
    number_index = offset // digits_per_number
    position_in_number = offset % digits_per_number
    
    # عدد حاوی رقم
    target_number = start_number + number_index
    
    # استخراج رقم
    number_str = str(target_number)
    return int(number_str[position_in_number])

# محاسبه حاصل‌ضرب
p = 1
powers = [10**i for i in range(7)]  # [1, 10, 100, 1000, 10000, 100000, 1000000]

for n in powers:
    digit = ranGSaz(n)
    print(f"d_{n} = {digit}")
    p *= digit

print(f"Result = {p}")

# تست اضافی
print(f"ranGSaz(1905) = {ranGSaz(1905)}")

print("here im learning git")
print("git check success!")
