class reverse:
    """
    A class to reverse a given string.
    """

    def __init__(self, s=""):
        """
        The constructor method initializes the object with a string.

        :param s: The string to be stored. Defaults to an empty string.
        """
        self.s = s

    def get_reversed_string(self):
        """
        A method that returns the reversed version of the string stored in the object.
        """
        return self.s[::-1]

# --- Main Program Execution ---

# Prompt the user for input.
user_input_string = input("Enter a word to reverse: ")

# Create an instance of the 'reverse' class with the user's input.
# The user_input_string is passed as the 's' parameter to the constructor.
string_reverser = reverse(user_input_string)

# Call the get_reversed_string method to get the reversed string.
reversed_word = string_reverser.get_reversed_string()

# Print the original and reversed strings to the console.
print(f"Original word: {string_reverser.s}")
print(f"Reversed word: {reversed_word}")
