import random
choise = int(input("please select your choise from 0 1 and 2\n"))
computer = random.randint(0,2)
print(f"computer chose {computer}")


if choise >= 3 or choise<0:
    print("you make a wrong choice")
elif choise == 0 and computer ==2:
    print("you win")
elif choise == 2 and computer == 0:
    print("you lose")
elif choise > computer:
    print("you win")
elif computer > choise:
    print("you lose")
elif computer == choise:
    print("both had a same choise hence this is a draw")

    
