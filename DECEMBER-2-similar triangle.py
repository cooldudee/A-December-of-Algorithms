s = input("Enter the sides of traingle 1: ").split()
s1 = list(map(int,s))

s3 = input("Enter the sides of traingle 2: ").split()
s2 = list(map(int,s3))

a = input("Enter the angles of traingle 1: ").split()
a1 = list(map(int,a))

a3 = input("Enter the angles of traingle 2: ").split()
a2 = list(map(int,a3))


if((s1[0]/s2[0])==(s1[1]/s2[1])==(s1[2]/s2[2])):
    print("sss")

elif((a1[0]==a2[0]) and (a1[1]==a2[1]) and (a1[2]==a2[2])):
    print("AAA")
    
elif((a1[0]==a2[2]) and (a1[1]==a2[1]) and (a1[2]==a2[0])):
    print("AAA")
    
elif(((s1[0]==s2[0]) and (a1[1]==a2[1]) and (s1[2]==s2[2])) or ((s1[1]==s2[1]) and (a1[0]==a2[0]) and (s1[2]==s2[2])) or ((s1[0]==s2[0]) and (a1[2]==a2[2]) and (s1[1]==s2[1]))):
    print("SAS")
