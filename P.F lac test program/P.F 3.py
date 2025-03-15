# Muhammad Usman khan
# Roll: 99
# Deparment= CS
#from calendar import month
q=int(input("press day 0 to 31 :"))
m=int(input("month is (13=January,14=February,3=March,4=April,5=May,6=June,7=July,8=August,9=September,10=October,11=November,12=December:):"))
y=int(input("enter a year:"))
#h = (q + abs(26*(m+1) /10) + y + abs(y/4) + 6*(abs(y/100)) + abs(y/400))%7
if(m==3 or m==4 or m==5 or m==6 or m==7 or m==8 or m==9 or m==10 or m==11 or m==12 or m==13 or m==14 ):
    # print("March")
#elif(m==4):
 #   print("April")
#elif(m==5):
 #   print("May")
#elif(m==6):
 #   print("June")
#elif(m==7):
 #   print("July")
#elif(m==8):
 #   print("August")
#elif(m==9):
 #   print("September")
#elif(m==10):
 #   print("October")
#elif(m==11):
   # print("November")
#elif(m==12):
   # print("December")
#elif(m==13):
    #print("January")
#elif(m==14):
    # print("February")
    print("")
else:
    print("invalid month date")

h = (q + abs(((m+1)*26 )/10) + y + abs(y/4)  + 6*(abs(y/100)) + abs(y/400))%7
a=int(h)
#print(a)
#w=int(input("Weak is (0 = Saturday, 1 = Sunday, 2 = Monday, 3=tuesday, 4=wednesday,5=thusday,6=friday):"))
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

#print("Day on %s/%s/%s was"%(m,q,y))