import random
import string

def generate_password(length):
    # Define the character sets to choose from
    alphabet = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation

    # Combine the character sets
    combined_characters = alphabet + numbers + special_characters

    # Generate a random password
    password = ''.join(random.choice(combined_characters) for i in range(length))

    return password

# Example usage
password = generate_password(12)
print(password)
