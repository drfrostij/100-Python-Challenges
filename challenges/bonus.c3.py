a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if b > c:
        print(b)
    else:
        print(c)
else:
    if a > c:
        print(a)
    else:
        print(c)
