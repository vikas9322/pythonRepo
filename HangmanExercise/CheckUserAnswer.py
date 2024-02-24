word_list = ["Mango","Apple","Kiwi"]

import random

chose_word = random.choice(word_list)

guess = input("Guess a Letter : ").lower()

# for letter in chose_word:
#     if letter == guess:
#         print("your right")
#     else:
#         print("your wrong")

# print("###################################")
# Replacing the blanks with guesses 
# new_list = []
# for letter in chose_word:
#     if letter == guess:
#         new_list.append(letter)
#     else:
#         new_list.append("_")
# print(new_list)

# print("###################################")

display = []

for _ in range(len(chose_word)):
    display += "_"
print(display)

guess = input("Guess a letter :").lower()

for position in range(len(chose_word)):
    letter = chose_word[position]
    if letter == guess:
        display[position] = letter


print(display)
