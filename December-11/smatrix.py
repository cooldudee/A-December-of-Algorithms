def printsp(er,ec,a):
    r = 0 
    c = 0 
    while (r < er and c < ec):
        for i in range(r,ec):
            print(a[r][i],"-->",end=" ")
        r = r + 1
        for i in range(r,er):
            print(a[i][ec - 1],"-->",end=" ")
        ec = ec - 1
        if (c < er and c < ec):
            for i in range(ec - 1,c - 1,-1):
                print(a[er - 1][i],"-->",end=" ")
            er = er - 1
            for i in range(er - 1,r - 1,-1):
                print(a[i][c],"-->",end=" ")
            c = c + 1
def main():
    n = int(input("Enter the number of rows and columns for the matrix:"))
    m = [[0] * n for i in range(n**n)]
    for i in range (n):
        for j in range(n):
            m[i][j]=int(input())
    printsp(n,n,m)
main()
