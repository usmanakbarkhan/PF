n=int(input("enter a number : "))
b=1
SUM=0
while n >= b :
    SUM = SUM + (b**2)
    print("SUM",SUM)
    b=b+1
# c = (int(n)*(int(n)+1))
c = n*(n+1)*(2*n +1)/6
print(c)