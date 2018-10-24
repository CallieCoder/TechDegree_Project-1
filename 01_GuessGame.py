import random 

CORRECT_GUESS = 34
attempts = [1] 

print("Hello, welcome to the Guessing Game! \nThe current high score is 250 points.")
guess = input("Guess a number from 1 - 100: ")
guess = int(guess)

def start_game():
	try:
		guess = input("Guess a number from 1 - 100: ")
		guess = int(guess)
	except ValueError:
		print("Invalid entry. Please enter numbers as integers only.")	
	
while guess != 34:
	if guess < 1 or guess > 100:
		print("This number is outside of the specified range. Stay between 1 - 100.")
		guess = input("Guess a number from 1 - 100: ")
		guess = int (guess)
		
	elif guess < 34:
		print("Sorry, {} is too low. Try a higher number.".format(guess))
		attempts.append(guess) 
		start_game
		guess = input("Guess a number from 1 - 100: ")
		guess = int (guess)
		
	elif guess > 34:
		print("Sorry, {} is too high. Try a lower number.".format(guess))
		attempts.append(guess) 
		start_game
		guess = input("Guess a number from 1 - 100: ")
		guess = int (guess)
		
print("That's the correct guess!!") 
print("You guessed {} times.".format(len(attempts)))
play_again = input("would you like to play again? (yes/no): ")

if play_again == "no":
	print("Thanks for playing today. Goodbye!")

elif play_again == "yes":
	start_game()

else:
	print("Please enter yes or no.")