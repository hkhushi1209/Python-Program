n = int(input("enter the number of rows: "))
print("Half Pyramid Pattern of Stars (*):")
for i in range(1, n+1):
    for j in range(0, i):
        print("*", end=" ")
    print("")