p=int(input("enter a number: "))
q=2
while p>q and p%q!=0:
    q = q + 1
if q<p:
    print("not prime number")
else:
    print("prime number")