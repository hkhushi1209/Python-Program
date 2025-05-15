def is_alphabet(char):
  """
  Checks if a given character is an alphabet (a-z or A-Z).

  Args:
    char: The character to be checked.

  Returns:
    True if the character is an alphabet, False otherwise.
  """
  if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
    return True
  else:
    return False

# Get input from the user
user_input = input("Enter a character: ")

# Check if the input has exactly one character
if len(user_input) == 1:
  character = user_input[0]
  if is_alphabet(character):
    print(f"'{character}' is an alphabet.")
  else:
    print(f"'{character}' is not an alphabet.")
else:
  print("Please enter a single character.")