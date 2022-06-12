# Incorporate the random library
import random
def tie_results():
    print("Try again")

while True:
    # Print Title
 print("Are you ready to ROCK PAPER SCISSORS!!!")
#player selection
 user_action = input("Make your Choice: [R]ock, [P]aper, [S]cissors? ")

# Specify the three options
 options = ["R", "P", "S"]

# Computer Selection
 computer_action = random.choice(options)

 print(f"\nYOU {user_action} : PLAYER {computer_action}\n")
# Run Conditionals
 if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        tie_results()
 elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
 elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
 elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

 play_again = input("Play again? (y/n): ")
 if play_again.lower() != "y":
        break
    
    