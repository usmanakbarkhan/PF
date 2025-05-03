
def small(x,y,z):
    a=0
    if x < y and x < z:
       print("x is small :", x )
    elif y < x and y < z:
         print("y is small :", y )
    else:
         print("x is small :", z )
    return

def avarage(x,y,z):
    sum = x + y + z
    avarages = sum / 3
    print("avarage is : ", avarages)
    return

x=int(input("enter a number x :"))
y=int(input("enter a number y :"))
z=int(input("enter a number z :"))
b = small(x,y,z)
c = avarage(x,y,z)
