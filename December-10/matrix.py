import numpy
print("DETERMINANT OF A MATRIX")
n = int(input("Enter the no of rows of columns"))
c =[]
for i in range(n):
    a =[]
    for j in range(n):
        b = int(input(f"Enter the {i+1}rowth {j+1}th number"))
        a.append(b)
    c.append(a)
print(c)
print(int(numpy.linalg.det(c)))
