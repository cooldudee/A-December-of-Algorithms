s = input("Enter the word")
n = int(input("Enter the number"))
a =[]
for i in s:
    print(chr(ord(i)+n),end='')
