  # Use float to handle both integers and decimals
num = float(input("Enter a number: "))  # Use float to handle both integers and decimals
# Check if the number is greater than zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") #handles the edge case where the number is 0