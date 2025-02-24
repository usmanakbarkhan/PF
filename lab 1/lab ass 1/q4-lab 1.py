import math
Ax=float(input("enter a x_1 value:"))
Bx=float(input("enter a x_2 value:"))
Ay=float(input("enter a y_1 value:"))
By=float(input("enter a y_2 value:"))
D= math.sqrt((Ax-Bx)**2 + ((Ay-By)**2))
if(Ax>=0 and Ay>=0):
    print("x_1 and y_1 lies in 1th Quadrants")
elif(Ax<=0 and Ay>=0):
    print("x_1 and y_1 lies in 2th Quadrants")
elif(Ax<=0 and Ay<=0):
    print("x_1 and y_1 lies in 3th Quadrants")
elif(Ax>=0 and Ay<=0):
    print("x_1 and y_1 lies in 4th Quadrants")

if(Bx>=0 and By>=0):
    print("x_2 and y_2 lies in 1th Quadrants")
elif(Bx<=0 and By>=0):
    print("x_2 and y_2 lies in 2th Quadrants")
elif(Bx<=0 and By<=0):
    print("x_2 and y_2 lies in 3th Quadrants")
elif(Bx>=0 and By<=0):
    print("x_2 and y_2 lies in 4th Quadrants")
