num=int(input("enter a number how many you write : "))
a = []
count1 = 0
for j in range(0,num):
    for i in range(0,1):
        b = int(input("enter a number: "))
        a.append(b)
n = len(a)
print("after sorting= ",a)
a.sort()
print("befor sorting= ",a)
if n % 2 == 1:
    eng = (n + 1) // 2
    median = a[eng - 1]
else:
    median = ((n // 2) + ((n // 2) + 1)) // 2
print(median)


