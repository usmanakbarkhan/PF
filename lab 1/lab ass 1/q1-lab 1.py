
byte=int(input("enter a number in byte:"))
gigabyte=  (1024*1024*1024)
megabyte=  (1024 * 1024)
kilobyte= (1024)
a=kilobyte
b=megabyte
c=gigabyte
if(byte>=c):
    h=int(byte/c)
    i=byte%c
    #print(i)
    if(i>=b):
        j=int(i/b)
        k=i%b
        #print(k)
        if(k>=a):
            l=int(k/a)
            m=k%a
            # print(m)
            print("%s GB %s MB %s KB %s Byte "%(h,j,l,m))
        else:
            print("%s KB %s Byte"%(h,i))
    else:
        print("%s MB %s Bytes"%(h))
elif(byte>=b):   ### mb
    d=int(byte/b)       ###mb
    e=byte%b     #remaining byte
     #print(e)
    if(e>=a):     #kb
         f=int(e/a)          ####kb
         g=e%a                #### bytes
         #print(g)
         print("%s MB %s Kb %s Byte"%(d,f,g))
    else:
         print("%s MB %s Byte"%(d,e))
elif(byte>=a):
    n = int(byte / a)
    o = byte % a
    print("%s KB %s Bytes" % (n, o))
else:
    print("%s Byte" % (byte))































































# if(byte>=b):   ### mb
#     d=int(byte/b)       ###mb
#     e=byte%b     #remaining byte
#     #print(e)
#     if(e>=a):     #kb
#         f=int(e/a)          ####kb
#         g=e%a                #### bytes
#         #print(g)
#         print("%s MB %s Kb %s Byte"%(d,f,g))
#     else:
#         print("%s MB %s Byte"%(d,e