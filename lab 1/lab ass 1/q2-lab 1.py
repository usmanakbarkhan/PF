Ecat=float(input("enter is your Ecat mask out of 100:"))
inter=float(input("enter is your inter mask out of 1200:"))
matric=float(input("enter is your matric mask 1200:"))
Ecat_per=(Ecat/100)*33
inter_per=(inter/1200)*50
matric_per=(matric/1200)*17
aggregate=(Ecat_per+inter_per+matric_per)
print("aggregate is:{:.2f}".format(aggregate),"%")
