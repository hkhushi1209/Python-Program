print("Floyd's Triangle: ")
n = int(input("enter the number of rows: "))
number=1
for i in range(1,n+1):
    for j in range (0,i):
        print(number,end=" ",flush=True)
        number+=1
    print("")