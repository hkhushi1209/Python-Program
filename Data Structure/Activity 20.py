ages = [19, 45, 12, 78]
for age in ages:
    if age < 18:
        print(age, "not allowed")
        # Use exit function
        # print(exit) # This line would print the exit built-in function object, which is usually not the intent.
        exit() # This will terminate the script execution
    else:
        print(age, "allowed")