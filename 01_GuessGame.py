CORRECT_GUESS = 34
attempts = [1] 

print("Hello, welcome to the Guessing Game! \nThe current high score is 250 points.")

while True:
	try:
		guess = int(input("Guess a number from 1 - 100: "))
	except ValueError:
		print("Invalid entry. Please enter numbers as integers only.")
	else:
		if guess < 1 or guess > 100:
			print("This number is outside of the specified range. Stay between 1 - 100.")
			
		elif guess < CORRECT_GUESS:
			print("Sorry, {} is too low. Try a higher number.".format(guess))
			attempts.append(guess) 
			
		elif guess > CORRECT_GUESS:
			print("Sorry, {} is too high. Try a lower number.".format(guess))
			attempts.append(guess) 
			
		elif guess == CORRECT_GUESS:
			print("That's the correct guess!!") 
			print("You guessed {} times.".format(len(attempts)))
			play_again = input("would you like to play again? (yes/no): ")
			if play_again == "no":
				break

print("Thanks for playing today. Goodbye!")

