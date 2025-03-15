a=3
c=5
b=1
for i in range(0,4):
    for j in range(a,4):
        print("*",end="")
        if (a == 1):
            a = 2
    for j in range(c):
        print(" ",end="")
    for j in range(b):
        print("*",end="")
    print()
    b = b + 1
    a = a - 1
    c = c - 2
