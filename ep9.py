s = 1000
for a in range(3,int((s-3)//3) +1):
    for b in range(a+1,int((s-1-a)//2) +1 ):
        c = s-a-b
        if a*a + b*b == c*c:
            break
print(a,b,c)
            
def find_pythagorean_triplets(s):
    for a in range(3, (s - 3) // 3 + 1):  # Outer loop for a
        for b in range(a + 1, (s - 1 - a) // 2 + 1):  # Inner loop for b
            c = s - a - b  # Calculate c
            if a**2 + b**2 == c**2:  # Check Pythagorean condition
                print(f"Pythagorean triplet + multiplication of it: ({a}, {b}, {c},{a*b*c})")

# Example usage
s = 1000  # Perimeter
find_pythagorean_triplets(s)

# s := 1000 // or whatever the perimeter should be
# for a := 3 to (s-3) div 3
# for b := (a+1) to (s-1-a) div 2
# c := s-a-b
# if c*c = a*a + b*b then
# output (a,b,c)
# end if
# end for
# end for