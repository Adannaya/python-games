import random

HANGMAN_ASCII = [
  """
   +---+
       |
       |
       |
     ===""",
  """
   +---+
   O   |
       |
       |
     ===""",
  """
   +---+
   O   |
   |   |
       |
     ===""",
  """
   +---+
   O   |
  /|   |
       |
     ===""",
  """
   +---+
   O   |
  /|\  |
       |
     ===""",
  """
   +---+
   O   |
  /|\  |
  /    |
     ===""",
  """
   +---+
   O   |
  /|\  |
  / \  |
     ==="""]

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()

def getRandomWord(wordlist):
	"""Returns a random string from the passed list of strings"""
	wordIndex = random.randint(0, len(wordlist) - 1)
	return wordlist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_ASCII[len(missedLetters)], "\n")

	print("Missed letters:", end=" ")
	for letter in missedLetters:
		print(letter, end=" ")
	print("\n")
	
	blanks = "_" * len(secretWord)
	
	# Replace blanks with correctly guessed letters
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
	
	# Show the secret word with spaces inbetween each letter
	for letter in blanks:
		print(letter, end=" ")
	print("\n")

def getGuess(alreadyGuessed):
	"""Returns the letter the player entered.
	Makes sure they only entered a single letter"""
	while True:
		guess = input("Guess a letter: ").lower()
		if len(guess) != 1:
			print("Please enter a single letter.")
		elif guess in alreadyGuessed:
			print("You have already guessed that letter. Choose again.")
		elif guess not in "abcdefghijklmnopqrstuvwxyz":
			print("Please enter a LETTER of the ENGLISH ALPHABET")
		else:
			return guess

def playAgain():
	"""Returns True if the player wishes to play again"""
	return input("Do you want to play again (yes or no)? ").lower().startswith("y")

print("H  A  N  G  M  A  N\n\n")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	diplayBoard(missedLetters, correctLetters, secretWord)

	# Let the player enter a letter
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess

		# Check if player has won
