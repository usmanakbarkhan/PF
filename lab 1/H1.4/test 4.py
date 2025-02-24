OriginalPrice=int(input("enter your original price:"))
if(OriginalPrice<12800):
    Discount=OriginalPrice*(7/100)
    print("Discount:%s"%(Discount))
    Finalprice=OriginalPrice-Discount
    print(Finalprice)
elif(OriginalPrice>=12800):
    Discount = OriginalPrice * (16 / 100)
    print(Discount)
    Finalprice = OriginalPrice - Discount
    print(Finalprice)
