def hash(s):
    l = []
    for i in s:
        l.append(ord(i))
    a = sum(l)
    print(a / len(s))
s = input("Enter a string:")
hash(s)
