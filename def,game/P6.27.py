column=10
row=9
b=[]
list1=[[1,2,3,4,5,6,7,8,9,10],
       [11,12,13,14,15,16,17,18,19,20],
       [21,22,23,24,25,26,27,28,28,30],
       [31,32,33,34,35,36,37,38,39,40],
       [41,42,43,44,45,46,47,48,49,50],
       [51,52,53,54,55,56,57,58,59,60],
       [61,62,63,64,65,66,67,68,69,70],
       [71,72,73,74,75,76,77,78,79,80],
       [81,82,83,84,85,86,87,88,89,90]]
list2=[[10,10,10,10,10,10,10,10,10,10],
       [10,10,10,10,10,10,10,10,10,10],
       [10,10,10,10,10,10,10,10,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [20,20,30,30,40,40,30,30,20,20],
       [20,30,30,40,50,50,40,30,30,20],
       [30,40,50,50,50,50,40,50,40,30]]
user=int(input("which you want to enter , seat ot seat price .if you want to enter seat then press 4 , or if you want to enter seat price then press 5 :"))
if user == 4:
    user2= int(input("enter a seat number :"))
    for i in range (len(list1)) :
        for j in range (column):
            q=list1[i][j]
            if q >0:
                if user2 == q :
                    price = list2[i][j]
                    print("price",price)
                    a=int(input("press 1 for  booking or press 2 for canceled :"))
                    if a== 1:
                        list2[i][j]=0
                        print("booking")
                    elif a== 2:
                        print("canceled")
                # else:
                #     print("")
            else:
                print("chose another seat")
elif user == 5:
    user3=int(input("enter a seat price :"))
    for k in range (len(list2)):
        for j in range (column):
            q = list2[k][j]
            print(q)
            if user3 == q:
                r = list1[k][j]
                b.append(r)
            # else:
            #     print("")
    print(b)
    seat = int(input("enter a seat number :"))
    for k in range (len(list1)):
        for j in range (column) :
            r = list1[k][j]
            if seat == r :
                a = int(input("press 1 for booking or press 2 for canceled :"))
                if a == 1:
                    list2[k][j]=0
                    print("booking")
                elif a == 2 :
                    print("canceled")
            # else:
            #     print("")
else:
    print("chose correct option")