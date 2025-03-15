a=int(input("enter a number: "))
Max=-1
while a>-1:
    if a>=Max:
        Max = a
        print(Max)
    a=int(input("enter a number"))
else:
     print("larger number is : ",Max)