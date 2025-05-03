
def repeat(string,n,delim):
    a = (string + delim) * n
    return a
string=input("enter a string : ")
n=int(input("enter a n : "))
delim=input("enter a delim : ")
e=repeat(string,n,delim)
print(e)