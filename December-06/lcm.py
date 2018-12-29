x = int(input("Enter first no:"))
y = int(input("Enter second no:"))
pro = (x * y)
n = 1000
a = [ ]
b = [ ]
for i in range(1,n):
    if x % i == 0:
        a.append(i)
for j in range(1,n):
    if y % j == 0:
        b.append(j)
if(set(a) and set(b)):
    common = (set(a) & set(b))
    gcd = (max(common))
lcm = pro // gcd    
print(lcm)
