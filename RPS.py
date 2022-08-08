import random
options = ["rock", "paper", "scissors"]
user_guess = 0
computer_guess = 0
Draw_count = 0

while True:
    
    
   user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
   if user_input == "q":
       break
   elif user_input not in options:
       continue 
   elif user_input in options:
        random_number = random.randint(0,2)
        computer_input =                    options[random_number]
        print("Computer_guess is: ", computer_input)
        if user_input == "rock" and computer_input == "scissors":
           print("You've Won")
           user_guess += 1
        elif user_input == "paper" and computer_input == "rock":
            print("You've Won")
            user_guess += 1
        elif user_input == "scissors" and computer_input == "paper":
            print("You've Won")
            user_guess += 1
        elif user_input == computer_input:
            print("Its a Draw")
            Draw_count += 1
        else:
            print("Computer Won")
            computer_guess += 1
            
     



print("Bye, Dude :)")
print("You've Won: ", user_guess, "times")
print("AI won: ", computer_guess, "times")
print("Draw count: ", Draw_count)
