n=int(input("enter a n value :"))
k = int(input("enter a k value :"))
if n>k:
    q = 1
    p=n
    r=n-k
    s=1
    c=1
    a=(n-k)+1
    while(p>=1):
        q=q*p
        if(p<=r):
            s=s*p
        if(p<=a):
           c = c * (n-p)
        p = p - 1
    g=n*c
    print(g)
    e=g*s
    print(e)
    f=(q/e)
    print(f)
else:
    print("please enter a k is small then n")