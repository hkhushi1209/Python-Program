print("Diamond Pattern ")
n = int(input("enter the number of rows: "))

# Top half
for i in range(1, n+1):
    for k in range(0,n-i+1):
        print(' ', end='')
    for j in range(1,2 * i):
        print('*', end='')
    print()

# Bottom half
for i in range(n-1, 0, -1):
    for k in range(0,n-i+1):
        print(' ', end='')
    for j in range(1,2 * i):
        print('*', end='')
    print()