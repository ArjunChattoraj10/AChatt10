import string, random

# Functions

def length_asker(): 
	"""
	This function is an i/o function that asks the user for a number that will be the length of the name, and returns the input.
	Any input that is not a positive integer is rejected and a sarcastic comment is printed, and the user is prompted for a different input.
	"""

	sarcastic = [
				"And no, you are not funny.",
				"Stop being this way.",
				"Not funny btw.",
				"Ha. Hahaha. HAHAHAHAHAHAHAHHAHAHAHA. \n \n \n \t Stop.",
				"Omg you're like so funny like omg."
				]


	length_input = input("\t Choose a length of the name: ")

	try:
		val = int(length_input)
	except ValueError:
		print("\t Input a positive integer in base 10 only. \n \t " + random.choice(sarcastic))
		length_input = length_asker()

	if not (float(length_input) > 0 and float(length_input) % 1 == 0):
		print("\t Input a positive integer in base 10 only. \n \t " + random.choice(sarcastic))
		length_input = length_asker()

	return(length_input)

def letter_asker():
	"""
	This function is an i/o function that the user for a choice of letter.
	Any input that is not a letter is rejected and a sarcastic comment is printed, with the user is prompted for a different input.
	"""
	sarcastic = [
				"Wow. Such a genius.",
				"You think you're funny, don't ya.",
				"HEY CARL CHECK OUT THIS OUT. \n \t IT'S LIKE SO FUNNY. \n \t COMEDY. \n \t GOLD.",
				"Don't be a weirdo.",
				"This is why no one likes you."
				]

	letter_in = input("\t Choose a letter CASE SENSITIVE: \n \t \t '1' for vowel -- a,e,i,o,u, \n \t \t '2' for consonants, \n \t \t '3' for any lowercase letter:, \n \t \t For a specific letter, simply type that letter: ")
	if len(letter_in) == 1 and letter_in in "123":
		return(letter_in)
	elif letter_in == "" or letter_in not in string.ascii_letters:
		print("\t Input 1,2,3 or a letter only. \n \t " + random.choice(sarcastic))
		letter_in = letter_asker()

def letter_generator(letter_input):
	"""
	This is a function to check what kind of letter should be used.

	Keyword arguments: 
	letter_input -- an input from the user.
		If the input argument is "1", then the function returns a random vowel.
		If the input argument is "2", then the function returns a random consonant.
		If the input argument is "3", then the function returns a random lowercase letter.
		For any other letter input, the function simply returns the letter.
	"""

	vowels = 'aeiou'
	consonants = 'bcdfghjklmnpqrstuvwxyz'

	if letter_input == "1":
		letter_out = random.choice(vowels)
	elif letter_input == "2":
		letter_out = random.choice(consonants)
	elif letter_input == "3":
		letter_out = random.choice(string.ascii_lowercase)
	else: # in the case user wants a specific letter
		letter_out = letter_input
	return(letter_out)



# Function call

length = length_asker()

i = 0
name = []

while i < int(length):
	letter = letter_asker()
	name.append(letter_generator(letter))
	i += 1

print("".join(name))

