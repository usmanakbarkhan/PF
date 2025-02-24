status=str(input("you are single or married:"))
income=int(input("what is your income:"))
if(status=='single'):
    if( income >= 0 and income < 50000):
        tex=(15/100)*income
        print(tex)
    elif(income >=50000 and income < 100000):
        tex=900+((15/100)*income)
        print(tex)
    elif(income >= 100000):
        tex=7500+((22/100)*income)
        print(tex)
elif(status=='married'):
    if(income >= 0 and income < 80000):
        tex = (15 / 100) * income
        print(tex)
    elif (income >= 80000 and income < 130000):
        tex = 1800 + ((15 / 100) * income)
        print(tex)
    elif(income >= 130000):
        tex=10000+((22/100)*income)
        print(tex)
