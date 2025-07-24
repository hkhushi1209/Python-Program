import random
import string

def generate_random_password(length=12):
    """
    Generates a random password consisting of lowercase letters, uppercase letters, and numbers.

    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: The generated random password.
    """
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password_list = [random.choice(characters) for _ in range(length)]
    random.shuffle(password_list)
    return "".join(password_list)

if __name__ == "__main__":
    password = generate_random_password()
    print(f"Generated random password: {password}")

    # You can specify a different length as well
    long_password = generate_random_password(length=16)
    print(f"Generated 16-character password: {long_password}")