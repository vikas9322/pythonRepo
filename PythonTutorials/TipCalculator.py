
billAmount = float(input("Enter the bill amount"))
numberOfPersons = int(input("Enter the number of members"))
contri = round((billAmount / numberOfPersons) * 1.12,2)

print(f"each person should conribute {contri}")