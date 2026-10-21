#Code 1st : dice simulator

import random

print("Welcome to Dice Simulator")

dice = random.randint(1, 6)

print("Dice result is:", dice)
"""Code 2nd : password genrator
import random
import string

print("Random Password Generator")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(characters)"""