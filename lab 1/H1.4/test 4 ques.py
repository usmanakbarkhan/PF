hour1=int(input("hour:"))
minute1=int(input("minute:"))
second1=int(input("second:"))
hour2= int(input("hour:"))
minute2 = int(input("minute:"))
second2 = int(input("second:"))

if(hour1<24):

    if(minute1<=60):

         if(second1<=60):
             print(hour1,minute1,second1)
         else:
             print("please enter correct second")
    else:
        print("please enter correct minute")

    if (hour2 < 24):

          if(minute2<=60):

              if(second2<=60):
                   print(hour2,minute2,second2)
              else:
                  print("please enter correct second")
          else:
              print("please enter correct minute")
    else:
        print("please enter correct hour")
else:
    print("please enter correct hour")
#print(" %s hour1 %s minute1 %s second1"%(hour1,minute1,second1))

if(hour1 >= hour2 and minute1 >= minute2 and second1 >= second2):
    print("time 1 is greater")
elif(hour2 >= hour1 and minute2 >= minute1 and second2 >= second1):
    print("time 2 is greater ")
else:
    print("Both time 1 and time 2 have same value")