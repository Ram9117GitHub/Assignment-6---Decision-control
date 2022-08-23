'''Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots.'''
a = int(input("Enter the a"))
b = int(input("Enter the b"))
c = int(input("Enter the c"))
d = b**2 -4*a*c # Formula of quadratic equation
if d>0:
    print("Real and distict roots")
elif d==0:
    print("Real & equal roots" )
else:
    print("Imaginary roots")