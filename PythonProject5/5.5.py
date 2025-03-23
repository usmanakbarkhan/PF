stu = int(input("enter a student number :"))
while stu<=0:
    if stu<0:
        stu = int(input("enter a student number :"))
else:
    if stu <= 20:
        print("student lie in 0-20")
    elif stu <= 40:
        print("student lie in 21-40")
    elif stu <= 60:
        print("student lie in 41-60")
    elif stu <= 80:
        print("student lie in 61-80")
    else:
        print("student lie in 81-100")
