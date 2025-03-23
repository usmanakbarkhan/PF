import random
num = []
while len(num)<20:
    ran=random.randint(1,20)
    if ran not in num :
      num.append(ran)
print(num)


