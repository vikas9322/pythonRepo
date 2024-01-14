import random
letters = ["a","b","c","d","e","f","g","h","i"]
numbers = ["0","1","2","3","4","5","6"]
symbols = ["!","@","#","$","%","^","&"]
passsword_letters = int(input("How many letters would you like in your password: \n"))
password_symbol = int(input("How may symbols would you like : \n"))
password_numbers = int(input("how many number would you like : \n"))

final_password = []

for char in range(1,passsword_letters + 1):
    final_password += random.choice(letters)
for char in range(1,password_symbol + 1):
    final_password += random.choice(numbers)
for char in range(1,password_symbol + 1):
    final_password += random.choice(symbols)
    
random.shuffle(final_password)

your_password = ""

for char in final_password:
    your_password += char

print(your_password)





