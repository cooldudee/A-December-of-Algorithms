Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> y = input("Enter the number")
x = list(map(int,y))
n = len(x)
sum1 = 0
sum2 = 0
for i in range(int(n/2)):
    sum1 = sum1 + x[i]
print(sum1)
for i in range(int(n/2),n):
    sum2 = sum2 + x[i]
print(sum2)
if sum1 == sum2:
    print(y,"is a lucky number")
else :
    print(y,"is not a lucky number")

