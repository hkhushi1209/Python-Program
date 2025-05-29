print("Pyramid Pattern ")
n = int(input("enter the number of rows:"))
for i in range(1, n+1):
    for k in range(0,n-i+1):
        print(' ', end='')
    for j in range(1,2 * i): # Stars (odd count)
        print('*', end='')
    print()