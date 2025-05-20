print("Sum of Natural Numbers Using For Loop.")
number = int(input("enter end number here: "))
sum = 0

for i in range(1, number + 1):
    sum += i

print("Sum of first", number, "natural numbers is:", sum)