n=int(input("enter a n value :"))
k = int(input("enter a k value :"))
if n>k:
   # section 1
    r = 1
    q = 1
    while n >= r:
        q = q * r
        r = r + 1
        print("n! = ",q)
    #section 2
    t = int((n - k))
    print(t)
    s = 1
    u = 1
    while t >= s:
        u = u * s
        s = s + 1
        print("(n-k)! = ",u)
    # section 3
    p=int(n-k+1)
    print(p)
    v = 1
    z = 1
    while p >= v:
        z = z*(n - v)
        v = v + 1
        print("(n-1)(n-2)......(n-k+1) = ",z)
    # section 4
    b= n * z
    print("(n-k+1)! = ",b)
    #section 5
    c=q/b
    print(c)
else:
    print("please enter a k is small then n")