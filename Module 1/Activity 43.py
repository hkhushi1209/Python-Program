def mirrored_right_angled_triangle(height):
    print("Mirrored Right Angled Triangle Pattern:")
height = int(input("enter the number of rows:"))
for i in range(1, height + 1):
    for j in range(height, i, -1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print("")