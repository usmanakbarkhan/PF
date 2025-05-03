
def first_digit (a):
    while a > 10:
        a = int(a / 10)
    print("the first digit of the argument :",a)
    return

def last_digit(a):
    b = a % 10
    print("the last digit of the argument :", b)
    return

def number_of_digits (a):
    count = 1
    while a > 10:
        a = int(a / 10)
        count = count + 1
    print("the number of digits in the argument :", count)
    return

a=int(input("enter a number : "))
c = first_digit(a)
d = last_digit(a)
e = number_of_digits(a)
