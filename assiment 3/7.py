import random
NUM=int(input("enter a number 1 to 10 :"))
if(NUM>0):
    com=random.randint(1,10)
    while(NUM!=com):
        if(NUM > com):
            print(" greater")
            NUM = int(input("again enter a number 1 to 10 :"))
        elif(NUM < com):
            print("smaller")
            NUM = int(input("again enter a number 1 to 10 :"))
        else:
            break
    print("good")
