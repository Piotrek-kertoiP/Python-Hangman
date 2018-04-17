import random
import sys

def checkCommandCorrectness():
	if len(sys.argv) >= 2:
		return True
	else: 
		print("Give me location of your dictionary\n")
		return False
	
def randomWord(filePath):
	plik = open(filePath, 'r')	
	wordsArray = plik.readlines()
	plik.close()
	size = len(wordsArray) - 1
	index = random.randint(0, size)
	return wordsArray[index]
	
def alreadyGuessed(guessedLetters, letter):
	asciiValue = ord(letter)
	if 96 < asciiValue and asciiValue < 123 and guessedLetters[ asciiValue - 97 ] == True :
		return True
	return False

def consists(array, element):
	for letter in array:
		if letter == element or letter == chr( ord(element) - 32 ):
			return True
	return False

def updateGuessedLetters(guessedLetters, letter):
	asciiValue = ord(letter)
	guessedLetters[ asciiValue - 97 ] = True

def updateUnknownWord(unknown, letter, answer):
	for i in range( len(answer) ):
		if answer[i] == letter or chr( ord(answer[i]) + 32) == letter:
			unknown[i] = letter

def answerIsComplete(unknown):
	for i in range( len(unknown) ):
		if unknown[i] == "_":
			return False
	return True

def upperCaseToLowerCase(letter):	
	if ord(letter) < 93:
		letter = chr( ord(letter) + 32 )
	return letter

def blankArrayForPlayersGuesses( length ):
	array = []	
	for i in range(0, length - 1):
		array.append('_')
	return array

def alphabetGuessInitFalse():
	guessedLetters = []	
	for i in range(26):
		guessedLetters.append(False)
	return guessedLetters
		
def itsLetter(letter):
	if 97 <= ord(letter) and ord(letter) <= 122:
		return True
	return False


def game():
	flag = checkCommandCorrectness()
	if flag == True:
		filePath = sys.argv[1]
	
	while(flag):
		chancesLeft = 3	
		try:		
			answer = randomWord(filePath)
		except FileNotFoundError:
			print("This file wasn't found\n")
			break

		print("The answer is: " + answer)		#wykomentować
		
		unknown = blankArrayForPlayersGuesses( len(answer) )
		guessedLetters = alphabetGuessInitFalse()
							
		while(chancesLeft > 0):
			if answerIsComplete(unknown) == True:			
				print("Congratulations! You won! The answer was " + str(answer) +"\n")
				break

			print("Your answer is: " + str(unknown) )			
			letter = input('Give me a letter\n')
			
			letter = upperCaseToLowerCase(letter)

			if itsLetter(letter) == False:
				print("Give me a LETTER, please\n")
				continue		

			if alreadyGuessed(guessedLetters, letter) == True:
				print("You've already given me this letter. Choose another one\n")
				continue 
			
			updateGuessedLetters(guessedLetters, letter)

			if consists(answer, letter) == False:
				chancesLeft += -1
				print("Sorry, bad guess :( You have " + str(chancesLeft) + " chances left\n")
				continue		
			else:
				print("Good guess! You have " + str(chancesLeft) + " chances left\n") 
				updateUnknownWord(unknown, letter, answer)
		
		nextGame = input("Would you like to play one more time? y/n \n")
		if nextGame == "n":
			break


def main():
	game()


main()
