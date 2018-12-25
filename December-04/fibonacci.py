n = int(input("Enter the nth term"))
f = []
a = 0
b = 1
f.append(a)
f.append(b)
for i in range(2,n):
    c = a + b
    f.append(c)
    a = b
    b = c
print("The nth term is:",f[n-1])
