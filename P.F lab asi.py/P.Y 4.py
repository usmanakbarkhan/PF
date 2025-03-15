from random import randint
x=randint(0,10)
y=int(input("enter a number:"))
if(x==y):
    print("correct")
elif(x<y):
    print("your number larger ")
elif(x>y):
    print("your number small")

