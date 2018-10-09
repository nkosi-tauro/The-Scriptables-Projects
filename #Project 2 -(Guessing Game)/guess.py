import time
print("Welcome To Guess or Lose:\n ")
print("The Goal is for you to figure out which one of the words below is correct (Remeber you ONLY have 3 guesses: \n")

print("noodles\nbeef\nBMW\nFord\npork\nnkosi\nlamb\nchicken\nporsche ")

secret_word = "chicken"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Enter Guess: ")
		guess_count += 1 
	else:
		out_of_guesses = True
	
if out_of_guesses:
	print("You failed to find the correct word, better luck next time")
else:
	print("Well done!!! ")

time.sleep(100)