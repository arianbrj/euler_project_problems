# for this problem we use dynamic programming and solve it esily!


pyrmid  = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

pyrmid = pyrmid.split("\n")

# print(pyrmid)


def string_cleaner(s1):
    if s1[0] == "0" and s1[1] != "0":
        s1 = s1.replace("0","")
    elif s1 == "00":
        s1.replace("00","0")    
    return s1

def sum_strings(s1,s2):
    s1,s2 = string_cleaner(s1),string_cleaner(s2)
    sum = int(s1) + int(s2)
    return sum


def list_to_string(row):
    s = ""
    for item in row:
        s += item + " "
    return s.strip()



for i in range(len(pyrmid)-2,0,-1):
    row = pyrmid[i].split(' ')
    newrow = []
    for j in range(len(row)):
        below_row = pyrmid[i+1].split(' ')
        s0 = string_cleaner(row[j])
        s1 = string_cleaner(below_row[j])
        s2 = string_cleaner(below_row[j+1])
        p01 = sum_strings(s0,s1)
        p02 = sum_strings(s0,s2)
        if p01 > p02:
            newrow.append(str(p01))
        else:
            newrow.append(str(p02))
    newrow = list_to_string(newrow)
    print(newrow)
    pyrmid.remove(pyrmid[-1])
    pyrmid.remove(pyrmid[-1])
    pyrmid.append(newrow)
    
    
    
a = int(pyrmid[0]) + int(pyrmid[1].split(' ')[0])
b = int(pyrmid[0]) + int(pyrmid[1].split(' ')[1])
if a > b:
    print(a)
else:
    print(b)
