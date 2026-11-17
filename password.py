import random
import string

def generate_password(length):
    characters = string.ascii_letters +string.digits + "%thi(8%#!@)"
    password =''.join(random.choice(characters) for _ in range(length))
    return password
print("RANDOM PASSWORD GENERATOR")
length= int(input("Enter password length"))
if length>=8:
    print("Your password is:",generate_password(length))
else:
    print("Password must be at least 8 characters!")