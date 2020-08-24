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
	# This function returns a random string from the passed list of strings
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
	for letter in blanks
