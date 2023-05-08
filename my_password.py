from string import digits, ascii_letters, punctuation
import random


def generatePassword(length):
    password = ''
    while len(password) < length:
        password += random.choice(digits)
        password += random.choice(ascii_letters)
        password += random.choice(punctuation)
        return password
    

    password_length = int(input("Enter length of password: "))
    print(generatePassword(password_length))