import string
import random

def main(length: int) -> str:
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = "".join(random.choice(characters) for i in range(length))

    return password
