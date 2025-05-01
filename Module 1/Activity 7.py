# Function to convert lowercase word to uppercase
def convert_to_uppercase(word):
    return word.upper()

# Main program
if __name__ == "__main__":
    # Take input from the user
    lowercase_word = input("Enter a lowercase word: ")
    
    # Convert to uppercase
    uppercase_word = convert_to_uppercase(lowercase_word)
    
    # Display the result
    print("Uppercase word:", uppercase_word)