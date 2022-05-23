#Import random module
import random
#Initialize variables
computer_options = ["rock","paper","scissors"]
computer_choice = random.choice(computer_options)
user_choice  = input("Enter choice (rock/paper/scissors) : ")
# Run the game
while True:
    if computer_choice == "rock" and user_choice == "paper":
        print("Computer chose: ", computer_choice)
        print("You won! :D")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Computer chose: ", computer_choice)
        print("You lost! :c")
    elif computer_choice == "rock" and user_choice == "rock":
        print("Computer chose: ", computer_choice)
        print("Draw! :0")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("Computer chose: ", computer_choice)
        print("You won! :D")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Computer chose: ", computer_choice)
        print("You lost! :C")
    elif computer_choice == "paper" and user_choice == "paper":
        print("Computer chose: ", computer_choice)
        print("Draw! :0")
    elif computer_choice == "scissors" and user_choice == "scissors":
        print("Computer chose: ", computer_choice)
        print("Draw! :0")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Computer chose: ", computer_choice)
        print("You lost! :C")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("Computer chose: ", computer_choice)
        print("You won! :D")
    continueGame= input("Would you like to play again? (yes/no): ")
    if continueGame  == "yes":
        computer_choice = random.choice(computer_options)
        user_choice  = input("Enter choice (rock/paper/scissors) : ")
        
    elif continueGame == "no":
        print("Good game!")
        break