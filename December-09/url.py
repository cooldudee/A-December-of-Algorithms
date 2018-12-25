def https(string):
    if(string[0:8]=="https://"):
        return '1'
    else:
        return '0'
def url(string):
    if (".com" in string or ".net" in string or ".org" in s or ".in" in string):
        return "1"
    else :
        return '0'
string = input("Enter the string to check if it is an URL")
c = https(string)
if c =='1':
    u = url(string)
    if u =='1':
        print(f"{string} is an URL")
    else:
        print(f"{string} is not an URL")
else:
    print(f"{string} is not an URL")
