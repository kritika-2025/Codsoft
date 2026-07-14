import random
import string

# Ask the user for the password length
length = int(input("Enter the password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the password
print("\nGenerated Password:", password)
