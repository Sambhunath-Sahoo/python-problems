import math
#ax^2 + bx + c = 0
a = float(input("input the value for a :"))
b = float(input("input the value for b :"))
c = float(input("input the value for c :"))
d = b*b - 4*a*c
if d < 0:
    print("root are imaginary")
elif d == 0:
    r =  -b/(2*a)   
    print(f"the root is {r}")
else:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print(f"the roots are {r1},{r2}")

x = math.sqrt(25)
print(x)    