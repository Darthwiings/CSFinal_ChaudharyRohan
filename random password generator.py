#Import modules
import random
import string



#Function to generate random password

def random_password():
    characters  = list(string.ascii_lowercase + string.ascii_uppercase+string.digits+string.punctuation)
    length = int(input("Enter length of password : "))
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

print("Welcome to the password generator! \n")

# Loop to keep code running
while True:
    prompt1 = print("\n1.Would you like to generate a new password?\n2.End program?")
    prompt2  = int(input("Enter choice (1/2) : "))
    if prompt2 == 1:
        random_password()
        print(" \n1.Generate a new password? \n2. End program?")
        prompt3 = int(input("Enter option (1/2) : "))
        if prompt3 == 1:
            print("Exiting program.........")
            random_password()
        elif prompt3 == 2:
            break
    elif prompt2 == 2:
        print("Exiting program.........")
        break
    elif prompt2 != 1 or 2:
        print("\nPlease enter a valid option (1/2)\n")
                    
    
    

