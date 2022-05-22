#Import random module
import random
#Initialize variables
computer_options = ["rock","paper","scissors"]
computer_choice = random.choice(computer_options)
user_choice  = input("Enter choice (rock/paper/scissors) : ")
# Run the game
while True:
    if computer_choice == user_choice:
        print("You won! :D")
    else :
        print("You lost! :c")
    continueGame= input("Would you like to play again? (yes/no): ")
    if continueGame  == "yes":
        computer_choice = random.choice(computer_options)
        user_choice  = input("Enter choice (rock/paper/scissors) : ")
        
    elif continueGame == "no":
        print("Good game!")
        break
