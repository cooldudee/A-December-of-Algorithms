def IsApproximatelyEqual1(x,y):
    if(round(x)==round(y)):
        return '1'
    else:
        return '0'
def IsApproximatelyEqual2(x,y,t):
    t1 = abs(round(x-y,2))
    if (t1==t):
        return '1'
    else:
        return '0'
def switch(c):
    if c ==1:
        print("CHOICE is 1")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        a = IsApproximatelyEqual1(x,y)
        if a =='1':
            print("TRUE")
        else:
            print("FALSE")
            
    if c ==2:
        print("CHOICE is 2")
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        t = float(input("Enter the tolerance value: "))
        a = IsApproximatelyEqual2(x,y,t)
        if a =='1':
            print("TRUE")
        else:
            print("FALSE")
while(1):
    print("######ROUNDING OFF######")
    print("1.ROUND OFF WITHOUT TOLERANCE VALUE")
    print("2.ROUND OFF WITH TOLERANCE VALUE")
    print("3.QUIT")
    c = int(input("Enter the choice"))
    if (c!=1 and c!=2 and c!=3):
        print("Enter a valid choice")
    elif(c==3):
        break
    else:
        switch(c)
