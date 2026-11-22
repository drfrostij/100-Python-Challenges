x = 10
y = 20
z = 30

if x == 10:
    if y == 20:
        print("End of Nested If Block")
    else:
        print("End of Nested If-Else Block")
elif y == 20:
    print("Elif block")
    if z == 30:
        print("End of Nested If Block")
    else:
        print("End of Nested If-Else Block")
