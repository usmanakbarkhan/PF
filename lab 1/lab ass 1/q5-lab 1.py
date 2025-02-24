import cmath
import math
a=float(input("Enter a value of a:"))
b=float(input("Enter a value of b:"))
c=float(input("Enter a value of c:"))
D=(b**2)-(4*a*c)
if(D==0):
    print("Roots are real, equal and rational")
    d=math.sqrt(D)
    e =((-b) + d) /2 *a
    f = ((-b) - d) / 2 * a
    print(e,f)
elif(D>0):
    print("Roots are real, distinct and rational")
    d = math.sqrt(D)
    e = ((-b) + d) / 2 * a
    f = ((-b) - d) / 2 * a
    print(e, f)
elif(D<0):
    print("Roots are imaginary")
    d = cmath.sqrt(D)
    e = ((-b) + d) / 2 * a
    f = ((-b) - d) / 2 * a
    print(e, f)