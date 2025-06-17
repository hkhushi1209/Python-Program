try:
    age = int(input("Enter your age: "))
    if 0 < age < 130:
        print("Age entered is valid.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    else:
        print("Error: Age must be between 1 and 129.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")