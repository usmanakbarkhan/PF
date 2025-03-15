q=int(input("press day 0 to 31 :"))
m=int(input("month is (13=January,14=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December:):"))
y=int(input("enter a year:"))
if(m==3 or m==4 or m==5 or m==6 or m==7 or m==8 or m==9 or m==10 or m==11 or m==12 or m==13 or m==14 ):
    print("")
else:
    print("invalid month date")
h = (q + abs(((m + 1) * 26) / 10) + y + abs(y / 4) + 6 * (abs(y / 100)) + abs(y / 400)) % 7
a = int(h)
if(a==0):
    print("Day on %s/%s/%s was"%(m,q,y),"Saturday")
elif(a==1):
    print("Day on %s/%s/%s was"%(m,q,y),"Sunday")
elif(a==2):
    print("Day on %s/%s/%s was"%(m,q,y),"Monday")
elif(a==3):
    print("Day on %s/%s/%s was"%(m,q,y),"tuesday")
elif(a==4):
    print("Day on %s/%s/%s was"%(m,q,y),"wednesday")
elif(a==5):
    print("Day on %s/%s/%s was"%(m,q,y),"thusday")
elif(a==6):
    print("Day on %s/%s/%s was"%(q,m,y),"friday")