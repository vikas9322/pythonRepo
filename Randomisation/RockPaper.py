import random

def get_user_choice():
    # Get user input for their choice, with input validation
    while True:
        try:
            choice = int(input("Please select your choice from 0, 1, or 2: "))
            if 0 <= choice <= 2:
                return choice
            else:
                print("Invalid choice. Please choose a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on choices
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        return "You win!"
    elif user_choice > computer_choice:
        return "You win!"
    else:
        return "You lose!"

def main():
    # Main function to orchestrate the game
    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    # Run the game if the script is executed
    main()
