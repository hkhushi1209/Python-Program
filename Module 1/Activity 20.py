x = int(input("Enter Value of X: "))
y = int(input("Enter Value of Y: "))
z = int(input("Enter Value of Z: "))
if x > y and x > z:
    print("X is Greater")
elif y > x and y > z:
    print("Y is Greater")
else:
    print("Z is Greater")