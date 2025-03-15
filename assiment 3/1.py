S=int(input("start with:"))
E=int(input("end with:"))
i=5
count=0
while(S<=E):
    g=S*i
    print(g)
    count=count+1
    S=S+1
print(count)