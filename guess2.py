import random 

CORRECT_GUESS = 34
attempts = [1] 

print("Hello, welcome to the Guessing Game! \nThe current high score is 250 points.")

def start_game():
	guess = input("33-Guess a number from 1 - 100: ")
	guess = int(guess)
		
	while guess != CORRECT_GUESS:
		if guess < 1 or guess > 100:
			print("This number is outside of the specified range. Stay between 1 - 100.")
			guess = input("Guess a number from 1 - 100: ")
			guess = int (guess)
			
		elif guess < 34:
			print("Sorry, {} is too low. Try a higher number.".format(guess))
			attempts.append(guess)
			guess = input("Guess a number from 1 - 100: ")
			guess = int(guess) 
		
		elif guess > 34:
			print("Sorry, {} is too high. Try a lower number.".format(guess))
			attempts.append(guess)
			guess = input("Guess a number from 1 - 100: ")
			guess = int (guess) 
	
print("That's the correct guess!!") 
print("You guessed {} times.".format(len(attempts)))

play_again = input("would you like to play again? (yes/no): ")
if play_again == "yes" or "YES" or "Y":
	start_game()
elif play_again == "no" or "NO" or "n":
	print("Thanks for playing today. Goodbye!")
else:
	print("Please enter yes or no.")




