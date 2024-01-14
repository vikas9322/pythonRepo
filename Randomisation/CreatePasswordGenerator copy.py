import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
numbers = ["0", "1", "2", "3", "4", "5", "6"]
symbols = ["!", "@", "#", "$", "%", "^", "&"]

password_letters = int(input("How many letters would you like in your password: "))
password_symbols = int(input("How many symbols would you like: "))
password_numbers = int(input("How many numbers would you like: "))

# Generate the password based on the specified criteria
final_password = (
    random.choices(letters, k=password_letters)
    + random.choices(numbers, k=password_numbers)
    + random.choices(symbols, k=password_symbols)
)

# Shuffle the characters in the password
random.shuffle(final_password)

# Convert the list to a string
your_password = ''.join(final_password)

print("Your password:", your_password)
