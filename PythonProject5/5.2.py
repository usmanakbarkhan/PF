a=[]
sum=0
count1=0
for i in range(0,3):
   b=int(input("enter a number: "))
   sum=b+sum
   count1=count1+1
   a.append(b)
print("count1= ",count1)
print("a= ",a)
print("sum= ",sum)
x=int(sum/count1)
print("x= ",x)
c=0
sum2=0
count=0
for j in range(0,3):
    if a[j]>=x :
        c=a[j]
        sum2=c+sum2
        count=count+1
print("sum2=",sum2)
print("count= ",count)
avg=sum2/count
print("avg= ",avg)




