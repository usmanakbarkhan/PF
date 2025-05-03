u=0
m=0
a=[['_','_','_'],
   ['_','_','_'],
   ['_','_','_']]
for row in a:
    print(*row)
print("our Row start 0 and end with 2 , our column start with 0 and end with 2 :")
user1R=int(input("1 user1 Enter a Row number :"))
user1C=int(input("2 user1 Enter a column number :"))
while user1R >= len(a):
    user1R = int(input("1 user1 Enter a Row number :"))
while user1R < 0:
    user1R = int(input("1 user1 Enter a Row number :"))
while user1C >= len(a):
    user1C = int(input("2 user1 Enter a column number :"))
while user1C < 0:
    user1C = int(input("2 user1 Enter a column number :"))
a[user1R][user1C] = 1
for row in a:
    print(*row)
if a[user1R][user1C] == '_':
    a[user1R][user1C] = 1
    for row in a :
        print(*row)
for i in range (4):
    user2R=int(input("user2 Enter a Row number :"))
    user2C = int(input("user2 Enter a column number :"))
    while user2R >= len(a):
        user2R = int(input(" user2 Enter a Row number :"))
    while user2R < 0:
        user2R = int(input(" user2 Enter a Row number :"))
    while user2C >= len(a):
        user2C = int(input(" user2 Enter a column number :"))
    while user2C < 0:
        user2C = int(input(" user2 Enter a column number :"))
    # a[user2R][user2C] = 2
    # for row in a:
    #     print(*row)
    if a[user2R][user2C] == '_':
        a[user2R][user2C] = 2
        for row in a:
            print(*row)
    else:
        while a[user2R][user2C] != '_':
            user2R = int(input("user2 Enter a Row number :"))
            user2C = int(input("user2 Enter a column number :"))
            while user2R >= len(a):
                user2R = int(input(" user2 Enter a Row number :"))
            while user2R < 0:
                user2R = int(input(" user2 Enter a Row number :"))
            while user2C >= len(a):
                user2C = int(input(" user2 Enter a column number :"))
            while user2C < 0:
                user2C = int(input(" user2 Enter a column number :"))
        a[user2R][user2C] = 2
        for row in a:
            print(*row)
    if a[0][0] == 2  and a[0][1] == 2 and a[0][2] ==2:
        print("user2 winner")
        u=1
        break
    if a[1][0] == 2 and a[1][1] == 2 and a[1][2] ==2:
        print("user2 winner")
        u=1
        break
    if a[2][0] == 2 and a[2][1] == 2 and a[2][2] ==2:
        print("user2 winner")
        u=1
        break
    if a[0][0] == 2 and a[1][0] == 2 and a[2][0] ==2:
        print("user2 winner")
        u=1
        break
    if a[0][1] == 2 and a[1][1] == 2 and a[2][1] ==2:
        print("user2 winner")
        u=1
        break
    if a[0][2] == 2 and a[1][2] == 2 and a[2][2] ==2:
        print("user2 winner")
        u=1
        break
    if a[0][0] == 2 and a[1][1] == 2 and a[2][2] ==2:
        print("user2 winner")
        u=1
        break
    if a[0][2] == 2 and a[1][1] == 2 and a[2][0] ==2:
        print("user2 winner")
        u=1
        break
    use1R=int(input("use1 Enter a Row number :"))
    use1C = int(input("use1 Enter a column number :"))
    while use1R >= len(a):
        use1R = int(input("1 user1 Enter a Row number :"))
    while use1R < 0:
        use1R = int(input("1 user1 Enter a Row number :"))
    while use1C >= len(a):
        use1C = int(input("2 user1 Enter a column number :"))
    while use1C < 0:
        use1C = int(input("2 user1 Enter a column number :"))
    # a[use1R][use1C] = 1
    # for row in a:
    #     print(*row)
    if a[use1R][use1C] == '_':
        a[use1R][use1C] = 1
        for row in a:
            print(*row)
    else:
        while a[use1R][use1C] != '_':
            use1R = int(input("use1 Enter a Row number :"))
            use1C = int(input("use1 Enter a column number :"))
            while use1R >= len(a):
                use1R = int(input("1 user1 Enter a Row number :"))
            while use1R < 0:
                use1R = int(input("1 user1 Enter a Row number :"))
            while use1C >= len(a):
                use1C = int(input("2 user1 Enter a column number :"))
            while use1C < 0:
                use1C = int(input("2 user1 Enter a column number :"))
        a[use1R][use1C] = 1
        for row in a:
            print(*row)
    if a[0][0] == 1 and a[0][1] == 1 and  a[0][2] ==1:
        print("user1 winner ")
        m=1
        break
    if a[1][0] == 1 and a[1][1] == 1 and a[1][2] ==1:
        print("user1 winner ")
        m=1
        break
    if a[2][0] == 1 and a[2][1] == 1 and a[2][2] ==1:
        print("user1 winner ")
        m=1
        break
    if a[0][0] == 1 and a[1][0] == 1 and a[2][0] ==1:
        print("user1 winner ")
        m=1
        break
    if a[0][1] == 1 and a[1][1] == 1 and a[2][1] ==1:
        print("user1 winner ")
        m=1
        break
    if a[0][2] == 1 and a[1][2] == 1 and a[2][2] ==1:
        print("user1 winner ")
        m=1
        break
    if a[0][0] == 1 and a[1][1] == 1 and a[2][2] ==1:
        print("user1 winner ")
        m=1
        break
    if a[0][2] == 1 and a[1][1] == 1 and a[2][0] ==1:
        print("user1 winner ")
        m=1
        break
if u ==0 and m == 0:
    print("Draw")
