import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("please type a number that is larger than 0.")
        quit()
    
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
guess_list = []

while True:
    guesses += 1
    user_guess = input("Please guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess in guess_list:
        print("You already guessed that number!")
    elif user_guess > random_number:
        print("You were above the number!")
        guess_list.append(user_guess)
    elif user_guess < random_number:
        print("You were below the number!")
        guess_list.append(user_guess)
        
print("You got it in", guesses, "guesses")

play_again = input("Would you like to play again? (yes/no): ")
if play_again == "yes":
    exec(open("number_guesser.py").read())
else:
    print("Thanks for playing!")
    quit()