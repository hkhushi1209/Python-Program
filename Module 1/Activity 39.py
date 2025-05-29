n = int(input("enter the number of rows: "))
print("Inverted Right angled triangle (*):")
for i in range(n,0,-1):
    for j in range(0, i+1):
        print("*", end=" ")
    print("")