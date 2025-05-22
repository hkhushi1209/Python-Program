#Input the value of terms
n = int(input("Enter the value of terms: "))

sum = 0 #initialise
i = 1 #initialise
while i<=n: #loop will run from 1 to n
    sum +=i
    i +=1

print(sum)
print("\nSum of first",n,"natural numbers=", sum)